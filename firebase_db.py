import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

def get_firestore_client():
    credentials = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
    return firestore.Client(credentials=credentials, project=credentials.project_id)

def list_all_documents(collection_name):
    db = get_firestore_client()
    docs = db.collection(collection_name).stream()
    return [doc.id for doc in docs]

def save_form_data(collection_name, document_id, data):
    db = get_firestore_client()
    db.collection(collection_name).document(document_id).set(data)
