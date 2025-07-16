# pages/2_TMS_Info.py
import streamlit as st
from form_state import init_session
from firebase_db import fetch_dropdown, save_form_data


init_session()

st.markdown("""<h2 style='color:#006699;'>Section 2: TMS Info</h2>""", unsafe_allow_html=True)

dropdown_fields = {
    "TMS Vendor": "tmsVendor",
    "Access to TMS": "yes_no",
}

text_fields = ["DataLayer Name", "TMS Container ID"]

for label, table in dropdown_fields.items():
    options = fetch_dropdown(table)
    placeholder = f"Choose your {label}"
    options_with_placeholder = [placeholder] + options

    # Use unique key for widget, separate from session_state key
    key = f"select_{label}"
    default_value = st.session_state.get(label, placeholder)
    selected = st.selectbox(label, options_with_placeholder, index=options_with_placeholder.index(default_value) if default_value in options_with_placeholder else 0, key=key)

    # Store in session_state using correct key
    st.session_state[label] = selected if selected != placeholder else ""

for label in text_fields:
    widget_key = f"input_{label}"
    # Ensure the value is a string (not None)
    current_value = st.session_state.get(label, "")
    value = st.text_input(label, value=current_value, key=widget_key)
    # Update session state from widget only if changed
    if value != current_value:
        st.session_state[label] = value

