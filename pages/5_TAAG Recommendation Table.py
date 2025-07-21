import streamlit as st
from form_state import init_session
import pandas as pd
import os
import zipfile
from datetime import datetime
from PIL import Image
from utils.pdf_generator import generate_pdf 


st.set_page_config(layout="wide")
init_session()
st.markdown("<h2 style='color:#006699;'>TAAG Recommendation Adding Values</h2>", unsafe_allow_html=True)

image_dir = "generated"
os.makedirs(image_dir, exist_ok=True)

# Upload form
with st.form("upload_form"):
    uploaded_files = st.file_uploader("Choose image files", accept_multiple_files=True, key="uploaded_files")
    submitted = st.form_submit_button("Upload")

if submitted and uploaded_files:
    uploaded_image_paths = []

    for file in uploaded_files:
        if file.type.startswith("image/"):
            file_path = os.path.join(image_dir, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            uploaded_image_paths.append(file_path)

    st.session_state["uploaded_image_paths"] = uploaded_image_paths

   
# Show image previews
if "uploaded_image_paths" in st.session_state:
    st.markdown("### 🖼️ Image Previews:")
    cols = st.columns(3)
    for idx, img_path in enumerate(st.session_state["uploaded_image_paths"]):
        with cols[idx % 3]:
            st.image(Image.open(img_path), caption=os.path.basename(img_path), use_container_width =True)


# Initialize table only once
if "taag_table_data" not in st.session_state:
    st.session_state["taag_table_data"] = pd.DataFrame([
        {
            "Event Name": "",
            "Event Type": "",
            "Is the Event Triggered": False,
            "Custom Data": "",
            "Description": ""
        }
    ])

# Work with a temp copy to avoid immediate state overwrite
temp_df = st.session_state["taag_table_data"].copy()

# Editable table
edited_df = st.data_editor(
    temp_df,
    num_rows="dynamic",
    use_container_width=True,
    key="taag_table_editor"
)

# Update only if something changed (avoid refreshing state mid-edit)
if not edited_df.equals(st.session_state["taag_table_data"]):
    st.session_state["taag_table_data"] = edited_df
