import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

try:
    credentials = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
    db = firestore.Client(credentials=credentials, project=credentials.project_id)
    st.success("✅ Connected to Firestore")

    docs = db.collection("clients").stream()
    for doc in docs:
        st.write("Found doc ID:", doc.id)

except Exception as e:
    st.error(f"❌ Firestore error: {e}")
