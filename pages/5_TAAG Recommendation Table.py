import streamlit as st
from form_state import init_session
import pandas as pd
import os
import zipfile
from datetime import datetime
from PIL import Image

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

    # Zip and download
    zip_filename = f"uploaded_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_path = os.path.join(image_dir, zip_filename)
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for img_path in uploaded_image_paths:
            zipf.write(img_path, arcname=os.path.basename(img_path))

    st.success("Images uploaded and zipped!")
    st.markdown(f"[📥 Download {zip_filename}](sandbox:/mnt/data/generated/{zip_filename})")

# Show image previews
if "uploaded_image_paths" in st.session_state:
    st.markdown("### 🖼️ Image Previews:")
    cols = st.columns(3)
    for idx, img_path in enumerate(st.session_state["uploaded_image_paths"]):
        with cols[idx % 3]:
            st.image(Image.open(img_path), caption=os.path.basename(img_path), use_column_width=True)

# Initialize data
if "taag_table_data" not in st.session_state:
    st.session_state["taag_table_data"] = []

st.markdown("### 🧾 TAAG Table Entry")

# Add new row
with st.form("add_row_form"):
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        event_name = st.text_input("Event Name")
    with col2:
        event_type = st.text_input("Event Type")
    with col3:
        is_triggered = st.checkbox("Is Triggered?")

    custom_data = st.text_input("Custom Data")
    description = st.text_area("Description")

    submitted_row = st.form_submit_button("➕ Add to Table")

    if submitted_row and event_name and event_type:
        st.session_state["taag_table_data"].append({
            "Event Name": event_name,
            "Event Type": event_type,
            "Is the Event Triggered": is_triggered,
            "Custom Data": custom_data,
            "Description": description
        })
        st.success("✅ Row added!")

# Convert to DataFrame and show
if st.session_state["taag_table_data"]:
    df = pd.DataFrame(st.session_state["taag_table_data"])
    st.markdown("### 📊 Current Table State:")
    st.dataframe(df, use_container_width=True)
