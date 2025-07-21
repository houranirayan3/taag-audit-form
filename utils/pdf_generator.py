# utils/pdf_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os
from datetime import datetime
import pandas as pd


COVER_LOGO_PATH = "utils/cover_logo.png"
FOOTER_LOGO_PATH = "utils/logo.png"


def generate_pdf(session_state, filename="output.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom styles
    section_style = ParagraphStyle('SectionHeader', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#005C9E'), spaceAfter=10)
    field_label_style = ParagraphStyle('FieldLabel', parent=styles['Heading3'], fontSize=10, textColor=colors.black, spaceAfter=2, leading=14)
    field_value_style = ParagraphStyle('FieldValue', parent=styles['BodyText'], fontSize=10, spaceAfter=8, leading=12)

    flowables = []

    # Cover Page
    if os.path.exists(COVER_LOGO_PATH):
        img = Image(COVER_LOGO_PATH, width=2.5 * inch, height=1 * inch)
        flowables.append(Spacer(1, 150))
        flowables.append(img)
        flowables.append(Spacer(1, 40))

    client_name = session_state.get("Client", "[Client Name]")
    date_str = datetime.now().strftime("%B %d, %Y")

    flowables.append(Paragraph(f"<b>TAAG AUDIT REPORT:</b> {client_name}", section_style))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph(f"<b>Date:</b> {date_str}", field_value_style))
    flowables.append(PageBreak())

    # Audit Sections
    section_groups = {
        "Section Group 1": ["1. General Info", "2. TMS Info", "3. Audit Key Findings", "4. TAAG Recommendation", "5. Recommandation"],
        "Section Group 2": ["6. Enhanced Conversion", "7. Server-Side Tagging", "8. GMP/GA/GTM Linking", "9. CMP", "10. Web Analytics"]
    }

    all_sections = {
        "1. General Info": ["Client", "Market", "Urls", "Priority", "Website type", "Website category"],
        "2. TMS Info": ["TMS Vendor", "TMS Container ID", "Access to TMS", "DataLayer Name"],
        "3. Audit Key Findings": [
            "Link to Floodlight Report", "Key Event Tracked", "Untracked User Actions", "Incorrectly Implemented Tags", 
            "Redundant or Duplicate Tags", "Outdated Tags", "3rd Party Pixels Present", "Taxonomy", "Tag Sequencing Issue", 
            "DataLayer Issues", "Last Floodlight Audit", "Tag Format", "Page Load Options", "Summary"
        ],
        "4. TAAG Recommendation": [
            "Missing tags", "Incorrectly Implemented Tags1", "Redundant/Duplicated Tags", "Outdated Tags1", 
            "Load Performance", "Data Layer Issues", "Privacy Compliance", "Summary1"
        ],
        "5. Recommandation": [],
        "6. Enhanced Conversion": ["Enhanced Conversions", "Enhanced Attribution", "PII Hashing (email/phone)"],
        "7. Server-Side Tagging": ["Server side tagging in place", "Server side TMS container ID"],
        "8. GMP/GA/GTM Linking": ["DV360 Partner Linking", "GA property linking", "GTM container linking"],
        "9. CMP": ["Consent Mode Findings", "CMP Vendor", "Consent Type"],
        "10. Web Analytics": ["Vendor", "Partner ID", "Linked to Ad server"]
    }

    # Render sections
    for group, sections in section_groups.items():
        for section in sections:
            flowables.append(Paragraph(section, section_style))

            # Normal field values
            for field in all_sections[section]:
                label = Paragraph(f"<b>{field}</b>", field_label_style)
                value = Paragraph(str(session_state.get(field, "-")), field_value_style)
                flowables.extend([label, value])

            # Section 5 special case: Recommandation
            if section == "5. Recommandation":
                files = session_state.get("uploaded_file_names", [])
                if files:
                    flowables.append(Paragraph("<b>Uploaded Files</b>", field_label_style))
                    for name in files:
                        flowables.append(Paragraph(name, field_value_style))
                else:
                    flowables.append(Paragraph("❌ No uploaded files", field_value_style))

                df = session_state.get("taag_table_data")
                if isinstance(df, pd.DataFrame) and not df.empty:
                    flowables.append(Paragraph("<b>Event Table</b>", field_label_style))
                    table_data = [df.columns.tolist()] + df.values.tolist()
                    table = Table(table_data, repeatRows=1)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E3F2FD")),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica')
                    ]))
                    flowables.append(table)

                screenshots = session_state.get("screenshots", [])
                for img_path in screenshots:
                    if os.path.exists(img_path):
                        flowables.append(Image(img_path, width=4.5*inch, height=3*inch))

        flowables.append(PageBreak())

    # Build with footer logo
    def draw_footer(canvas, doc):
        if os.path.exists(FOOTER_LOGO_PATH):
            canvas.drawImage(FOOTER_LOGO_PATH, x=30, y=15, width=80, height=30, mask='auto')

    doc.build(flowables, onFirstPage=draw_footer, onLaterPages=draw_footer)
    return filename

