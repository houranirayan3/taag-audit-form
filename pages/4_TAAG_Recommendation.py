# pages/04_TAAG_Recommendation.py
import streamlit as st
from form_state import init_session

init_session()
st.markdown("<h2 style='color:#006699;'>Section 4: TAAG Recommendation</h2>", unsafe_allow_html=True)

text_fields = [
    "Missing tags",
    "Incorrectly Implemented Tags1",
    "Redundant/Duplicated Tags",
    "Outdated Tags1",
    "Load Performance",
    "Data Layer Issues",
    "Privacy Compliance",
    "Summary1"
]

placeholders = {
    "Missing tags": "Type your recommendations",
    "Incorrectly Implemented Tags1": "Type your recommendations",
    "Redundant/Duplicated Tags": "Type your recommendations",
    "Outdated Tags1": "Type your recommendations",
    "Load Performance": "Type your recommendations",
    "Data Layer Issues": "Type your recommendations",
    "Privacy Compliance": "Type your recommendations",
    "Summary1": "Type your recommendations"
}

for field in text_fields:
    current_value = st.session_state.get(field, "")
    value = st.text_area(
        label=field,
        value=current_value,
        height=150 if field == "Summary" else 100,
        placeholder=placeholders[field],
        key=f"input_{field}"
    )
    st.session_state[field] = value
