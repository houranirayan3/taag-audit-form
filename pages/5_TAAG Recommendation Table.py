import streamlit as st
from form_state import init_session
import pandas as pd
import os
import zipfile
from datetime import datetime

# Set page layout and section title
st.set_page_config(layout="wide")
init_session()
st.markdown("<h2 style='color:#006699;'>TAAG Recommendation Adding Values</h2>", unsafe_allow_html=True)

# Directory for saving images
os.makedirs("generated", exist_ok=True)

# Upload form
with st.form("upload_form"):
    uploaded_files = st.file_uploader("Choose image files", accept_multiple_files=True, key="uploaded_files")
    submitted = st.form_submit_button("Upload")

# Handle uploaded files
if submitted and uploaded_files:
    uploaded_image_paths = []

    for file in uploaded_files:
        if file.type.startswith("image/"):
            file_path = os.path.join("generated", file.name)
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            uploaded_image_paths.append(file_path)

    # Save to session
    st.session_state["uploaded_image_paths"] = uploaded_image_paths

    # Create ZIP file
    zip_filename = f"uploaded_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_path = os.path.join("generated", zip_filename)

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for img_path in uploaded_image_paths:
            zipf.write(img_path, arcname=os.path.basename(img_path))

    st.success("Images uploaded and zipped!")
    st.markdown(f"[📥 Download {zip_filename}](sandbox:/mnt/data/generated/{zip_filename})")

# Initialize table data only once
if "taag_table_data" not in st.session_state:
    st.session_state["taag_table_data"] = pd.DataFrame([{
        "Event Name": "",
        "Event Type": "",
        "Is the Event Triggered": False,
        "Custom Data": "",
        "Description": ""
    }])

# Show editable table (outside form so it doesn't reset)
edited_df = st.data_editor(
    st.session_state["taag_table_data"],
    num_rows="dynamic",
    use_container_width=True,
    key="editor_taag"
)

# Update session with edited table
st.session_state["taag_table_data"] = edited_df

# Optional: display a button to manually confirm table is saved
if st.button("✅ Confirm and Save Table"):
    st.success("Table saved in session!")
