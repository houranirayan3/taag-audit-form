# firebase_db.py
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

# Initialize Firestore client with Streamlit secrets
from google.cloud import firestore
from google.oauth2 import service_account
import streamlit as st

def get_firestore_client():
    # Copy the secrets to a new mutable dictionary
    key_dict = dict(st.secrets["firestore"])

    # Replace literal \n with actual newlines
    key_dict["private_key"] = key_dict["private_key"].replace("\\n", "\n")

    # Initialize credentials and client
    credentials = service_account.Credentials.from_service_account_info(key_dict)
    return firestore.Client(credentials=credentials, project=credentials.project_id)


# Save form data to Firestore (optional usage)
def save_form_data(collection_name, data_dict):
    db = get_firestore_client()
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data_dict)

# Example fetch function for dropdowns
# (Not needed if calling directly inside the pages)
def fetch_dropdown(collection_name):
    db = get_firestore_client()
    docs = db.collection(collection_name).stream()
    return [doc.id for doc in docs]
