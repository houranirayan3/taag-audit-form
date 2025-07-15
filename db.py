# db.py
import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Houranir2!",  # Replace with your actual MySQL root password
        database="taag_audit"
    )

def fetch_dropdown(table_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT value FROM {table_name}")
        results = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        st.warning(f"⚠️ Failed to fetch data from {table_name}: {e}")
        return []
