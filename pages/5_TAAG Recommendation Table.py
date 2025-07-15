import streamlit as st
from form_state import init_session
from db import fetch_dropdown
import pandas as pd
import os

init_session()

st.set_page_config(layout="wide")
st.markdown("<h2 style='color:#006699;'>TAAG Recommendation Adding Values</h2>", unsafe_allow_html=True)

# File upload
with st.form("upload_form"):
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, key="uploaded_files")
    submitted = st.form_submit_button("Upload")

if submitted and uploaded_files:
    file_names = [f.name for f in uploaded_files]
    st.session_state["uploaded_file_names"] = file_names

    uploaded_image_paths = []
    for file in uploaded_files:
        if file.type.startswith("image/"):
            path = os.path.join("generated", file.name)
            with open(path, "wb") as f:
                f.write(file.getbuffer())
            uploaded_image_paths.append(path)

    st.session_state["uploaded_image_paths"] = uploaded_image_paths

# Initialize table only once
if "taag_table_data" not in st.session_state:
    st.session_state["taag_table_data"] = pd.DataFrame(
        [
            {
                "Event Name": "",
                "Event Type": "",
                "Is the Event Triggered": False,
                "Custom Data": "",
                "Description": ""
            }
        ]
    )

# Editable table (outside form so it's not reset)
edited_df = st.data_editor(
    st.session_state["taag_table_data"],
    num_rows="dynamic",
    use_container_width=True,
    key="editor_taag"
)

st.session_state["taag_table_data"] = edited_df
