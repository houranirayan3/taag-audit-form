# pages/3_Audit_Findings.py
import streamlit as st
from form_state import init_session
from db import fetch_dropdown

init_session()

st.markdown("<h2 style='color:#006699;'>Section 3: Audit Key Findings</h2>", unsafe_allow_html=True)

# Dropdown values from DB
page_load_options = fetch_dropdown("page_load_options")
tag_formats = fetch_dropdown("tag_formats")

# Organize fields into columns
col1, col2 = st.columns(2)

with col1:
    left_text_fields = [
        "Link to Floodlight Report",
        "Key Event Tracked",
        "Untracked User Actions",
        "Incorrectly Implemented Tags",
        "Redundant or Duplicate Tags"
    ]
    for label in left_text_fields:
        value = st.text_area(label, value=st.session_state.get(label, ""), key=f"input_{label}")
        st.session_state[label] = value

with col2:
    right_text_fields = [
        "Outdated Tags",
        "3rd Party Pixels Present",
        "Taxonomy",
        "Tag Sequencing Issue",
        "DataLayer Issues"
    ]
    for label in right_text_fields:
        value = st.text_area(label, value=st.session_state.get(label, ""), key=f"input_{label}")
        st.session_state[label] = value

# Date picker field
date_label = "Last Floodlight Audit"
date_value = st.session_state.get(date_label)
if date_value:
    date_value = st.date_input(date_label, value=date_value, key=f"input_{date_label}")
else:
    date_value = st.date_input(date_label, key=f"input_{date_label}")
st.session_state[date_label] = date_value

# Below the columns
st.markdown("<br>", unsafe_allow_html=True)
dropdown_fields = {
    "Tag Format": tag_formats,
    "Page Load Options": page_load_options,
}

for label, options in dropdown_fields.items():
    placeholder = f"Choose your {label}"
    options_with_placeholder = [placeholder] + options

    current_value = st.session_state.get(label, placeholder)
    selected = st.selectbox(label, options_with_placeholder,
                            index=options_with_placeholder.index(current_value)
                            if current_value in options_with_placeholder else 0,
                            key=f"select_{label}")

    st.session_state[label] = selected if selected != placeholder else ""

# Summary field
summary = st.text_area("Summary", value=st.session_state.get("Summary", ""), key="input_Summary")
st.session_state["Summary"] = summary
