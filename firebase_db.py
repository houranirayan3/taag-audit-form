import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["FIREBASE"])
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Example: fetch dropdown values from a collection
def fetch_dropdown(collection_name):
    docs = db.collection(collection_name).stream()
    return [doc.id for doc in docs]

# Example: save form data
def save_form_data(collection, doc_id, data):
    db.collection(collection).document(doc_id).set(data)

# Example: read data
def read_form_data(collection, doc_id):
    doc = db.collection(collection).document(doc_id).get()
    return doc.to_dict() if doc.exists else None
