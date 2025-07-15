# form_state.py
import streamlit as st

def init_session():
    keys = [
        # Section 1 - General Info
        "Client", "Market", "Urls", "Priority", "Website type", "Website category",

        # Section 2 - TMS Info
        "TMS Vendor", "TMS Container ID/IDs", "Access to TMS", "DataLayer name",

        # Section 3 - Audit Key Findings
        "Last floodlight audit", "Link to floodlight report", "List of all active/inactive floodlights tags in the ad server",
        "Key event tracked", "Untracked user actions", "Incorrectly implemented tags", "Redundant or duplicate tags",
        "Outdates tags", "3rd party pixels present", "Page load condition", "Taxonomy", "Tag formats(floodlights)",
        "Tag sequencing issue", "DataLayer issues", "Summary",

        # Section 4 - TAAG Recommendation
        "Missing tags", "Incorrectly Implemented Tags", "Redundant/Duplicated Tags", "Outdated Tags",
        "Load Performance", "Data Layer Issues", "Privacy Compliance", "Summary",

        # Section 5 - Enhanced Conversion
        "Enhanced Conversions", "Enhanced Attribution", "PII Hashing (email/phone)",

        # Section 6 - SST
        "Server side tagging in place", "Server side TMS container ID",

        # Section 7 - GMP-GA-GTM Linkings
        "DV360 Partner Linking", "GA property linking", "GTM container linking",

        # Section 8 - CMP
        "Consent Mode Findings", "CMP Vendor", "Consent Type",

        # Section 9 - Web Analytics
        "Vendor", "Partner ID", "Linked to Ad server"
    ]

    for key in keys:
        if key not in st.session_state:
            st.session_state[key] = None

    if "pdf_generated" not in st.session_state:
        st.session_state["pdf_generated"] = False
    if "pdf_path" not in st.session_state:
        st.session_state["pdf_path"] = ""
    if "pdf_name" not in st.session_state:
        st.session_state["pdf_name"] = ""
