import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

# Load credentials from secrets
creds = service_account.Credentials.from_service_account_info(
    st.secrets["firestore"]
)

# Initialize Firestore client
db = firestore.Client(credentials=creds, project=st.secrets["gcp_service_account"]["project_id"])

