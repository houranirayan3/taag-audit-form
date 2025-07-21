import streamlit as st
from form_state import init_session
from firebase_db import fetch_dropdown, save_form_data

# Page settings
st.set_page_config(page_title="General Info", layout="wide")
st.markdown("<h2 style='color:#006699;'>Section 1: General Info</h2>", unsafe_allow_html=True)

# Initialize session state
init_session()

# Define dropdown fields and their corresponding Firestore collections
dropdown_fields = {
    "Client": "clients",
    "Market": "markets",
    "Priority": "priorities",
    "Website type": "website_types",
    "Website category": "website_categories"
}

# Define text fields
text_fields = ["Urls"]

# Render dropdown fields
for label, collection in dropdown_fields.items():
    options = fetch_dropdown(collection)
    placeholder = f"Choose your {label}"
    options_with_placeholder = [placeholder] + options

    current_value = st.session_state.get(label, "")
    index = options_with_placeholder.index(current_value) if current_value in options else 0

    selected = st.selectbox(label, options_with_placeholder, index=index, key=f"select_{label}")

    # Save selection to session_state only if it's not the placeholder
    st.session_state[label] = selected if selected != placeholder else ""

# Render text input fields
for label in text_fields:
    current_value = st.session_state.get(label, "")
    value = st.text_input(label, value=current_value, key=f"input_{label}")
    st.session_state[label] = value

