# pages/10_Preview.py
import streamlit as st
import os
from datetime import datetime
from utils.pdf_generator import generate_pdf
from form_state import init_session

st.set_page_config(page_title="Preview & Submit", layout="wide")
st.title("\U0001F4CB Preview & Submit Report")

init_session()  # Ensure all session keys are initialized

audit_sections = {
    "1. General Info": ["Client", "Market", "Urls", "Priority", "Website type", "Website category"],
    "2. TMS Info": ["TMS Vendor", "TMS Container ID", "Access to TMS", "DataLayer Name"],
    "3. Audit Key Findings": [
        "Link to Floodlight Report", "Key Event Tracked", "Untracked User Actions", "Incorrectly Implemented Tags", "Redundant or Duplicate Tags", "Outdated Tags", "3rd Party Pixels Present", "Taxonomy", "Tag Sequencing Issue", "DataLayer Issues", "Last Floodlight Audit", "Tag Format", "Page Load Options", "Summary"
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

st.subheader("\U0001F9FE Audit Summary Preview")

for section, fields in audit_sections.items():
    with st.expander(section, expanded=True):
        if section == "5. Recommandation":
            # Uploaded files
            uploaded_files = st.session_state.get("uploaded_file_names", [])
            if uploaded_files:
                st.markdown("**Uploaded Files:**")
                for name in uploaded_files:
                    st.markdown(f"- [{name}](uploads/{name})")
            else:
                st.markdown("")

            # Event table
            df = st.session_state.get("taag_table_data")
            if df is not None and not df.empty:
                st.markdown("**Event Table:**")
                st.dataframe(df, use_container_width=True)
            else:
                st.markdown("❌ Table is empty")
        else:
            for field in fields:
                value = st.session_state.get(field, "")
                if isinstance(value, str):
                    value = value.strip()
                if value == "":
                    st.markdown(f"❌ **{field}**: _Missing_")
                elif isinstance(value, str) and "\n" in value:
                    st.markdown(f"**{field}**:")
                    st.markdown(
                        "<div style='padding-left:1em; font-family:monospace;'>" +
                        "<br>".join(value.splitlines()) +
                        "</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"**{field}**: {value}")


# Trigger PDF generation
if st.button("\U0001F4C4 Generate PDF Report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"TAAG_Audit_Report_{timestamp}.pdf"
    path = generate_pdf(st.session_state, filename=filename)
    st.session_state["pdf_path"] = path
    st.session_state["pdf_name"] = filename
    st.session_state["pdf_generated"] = True
    st.success("✅ PDF generated successfully!")

if st.session_state.get("pdf_generated") and os.path.exists(st.session_state["pdf_path"]):
    with open(st.session_state["pdf_path"], "rb") as f:
        st.download_button("⬇️ Download PDF", data=f, file_name=st.session_state["pdf_name"], mime="application/pdf")
