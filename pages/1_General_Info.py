

from form_state import init_session
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

def get_firestore_client():
    credentials = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
    return firestore.Client(credentials=credentials, project=credentials.project_id)


def load_user_refresh_token():
    db = get_firestore_client()
    doc = db.collection("clients").document("Ancestry").get()
    return doc.to_dict()["Client name"] if doc.exists else None

st.set_page_config(page_title="General Info", layout="wide")
st.markdown("<h2 style='color:#006699;'>Section 1: General Info</h2>", unsafe_allow_html=True)

init_session()

dropdown_fields = {
    "Client": "clients",
    "Market": "markets",
    "Priority": "priorities",
    "Website type": "website_types",
    "Website category": "website_categories"
}

text_fields = ["Urls"]

def main():
    st.write(load_user_refresh_token())

# # Dropdowns with non-selectable placeholder
# for label, table in dropdown_fields.items():
#     options = fetch_dropdown(table)
#     placeholder = f"Choose your {table.replace('_', ' ')}"
#     options_with_placeholder = [placeholder] + options

#     current_value = st.session_state.get(label, "")
#     if current_value not in options:
#         current_value = placeholder

#     selected = st.selectbox(label, options_with_placeholder, index=options_with_placeholder.index(current_value), key=f"select_{label}")

#     # Only save if a real option is selected
#     if selected != placeholder:
#         st.session_state[label] = selected
#     else:
#         st.session_state[label] = ""  # Or None, depending on your needs

# # Text fields
# for label in text_fields:
#     current_value = st.session_state.get(label, "")
#     value = st.text_input(label, value=current_value, key=f"input_{label}")
#     st.session_state[label] = value
