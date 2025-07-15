# pages/6_Enhanced_Conversion/SST/Analytics.py
import streamlit as st
from form_state import init_session
from db import fetch_dropdown

init_session()

# Section 6: Enhanced Conversion
st.markdown("<h2 style='color:#006699;'>Section 5: Enhanced Conversion</h2>", unsafe_allow_html=True)

dropdown_fields = {
    "Enhanced Conversions": "yes_no",
    "Enhanced Attribution": "yes_no",
    "PII Hashing (email/phone)": "yes_no"
}

col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for (label, table), col in zip(dropdown_fields.items(), columns):
    with col:
        try:
            options = fetch_dropdown(table)
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch data from {table}: {e}")
            options = []

        placeholder = f"Choose an option"
        options_with_placeholder = [placeholder] + options
        current_value = st.session_state.get(label, placeholder)

        selected = st.selectbox(
            label,
            options_with_placeholder,
            index=options_with_placeholder.index(current_value)
            if current_value in options_with_placeholder else 0,
            key=f"select_{label}"
        )

        st.session_state[label] = selected if selected != placeholder else ""

# Spacer between sections
st.markdown("---")

# Section 7: Server-Side Tagging
st.markdown("<h2 style='color:#006699;'>Section 6: Server-Side Tagging</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    sst_label = "Server side tagging in place"
    current_sst = st.session_state.get(sst_label, "Choose an option")
    sst_options = ["Choose an option", "Yes", "No"]

    selected_sst = st.selectbox(
        "Server-side Tagging in Place",
        sst_options,
        index=sst_options.index(current_sst) if current_sst in sst_options else 0,
        key="select_sst"
    )
    st.session_state[sst_label] = selected_sst if selected_sst != "Choose an option" else ""

with col2:
    sst_id_label = "Server side TMS container ID"
    current_id = st.session_state.get(sst_id_label, "")
    value = st.text_input("Server side TMS Container ID", value=current_id, key="input_sst_id")
    st.session_state[sst_id_label] = value

# Spacer between sections
st.markdown("---")

# Section 8: GMP GA GTM

st.markdown("<h2 style='color:#006699;'>Section 7: GMP-GA-GTM Linkings</h2>", unsafe_allow_html=True)

dropdown_fields = {
    "DV360 Partner Linking": "yes_no",
    "GA property linking": "yes_no",
    "GTM container linking": "yes_no"
}

col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for (label, table), col in zip(dropdown_fields.items(), columns):
    with col:
        try:
            options = fetch_dropdown(table)
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch data from {table}: {e}")
            options = []

        placeholder = f"Choose an option"
        options_with_placeholder = [placeholder] + options
        current_value = st.session_state.get(label, placeholder)

        selected = st.selectbox(
            label,
            options_with_placeholder,
            index=options_with_placeholder.index(current_value)
            if current_value in options_with_placeholder else 0,
            key=f"select_{label}"
        )

        st.session_state[label] = selected if selected != placeholder else ""

# Spacer between sections
st.markdown("---")

# Section 9: CMP

st.markdown("<h2 style='color:#006699;'>Section 7: GMP-GA-GTM Linkings</h2>", unsafe_allow_html=True)

dropdown_fields = {
    "Consent Mode Findings": "yes_no",
    "CMP Vendor": "yes_no",
    "Consent Type": "yes_no"
}

col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for (label, table), col in zip(dropdown_fields.items(), columns):
    with col:
        try:
            options = fetch_dropdown(table)
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch data from {table}: {e}")
            options = []

        placeholder = f"Choose an option"
        options_with_placeholder = [placeholder] + options
        current_value = st.session_state.get(label, placeholder)

        selected = st.selectbox(
            label,
            options_with_placeholder,
            index=options_with_placeholder.index(current_value)
            if current_value in options_with_placeholder else 0,
            key=f"select_{label}"
        )

        st.session_state[label] = selected if selected != placeholder else ""

# Spacer between sections
st.markdown("---")

# Section 10: Web Analytics

st.markdown("<h2 style='color:#006699;'>Section 7: GMP-GA-GTM Linkings</h2>", unsafe_allow_html=True)

dropdown_fields = {
    "Vendor": "yes_no",
    "Partner ID": "yes_no",
    "Linked to Ad server": "yes_no"
}

col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for (label, table), col in zip(dropdown_fields.items(), columns):
    with col:
        try:
            options = fetch_dropdown(table)
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch data from {table}: {e}")
            options = []

        placeholder = f"Choose an option"
        options_with_placeholder = [placeholder] + options
        current_value = st.session_state.get(label, placeholder)

        selected = st.selectbox(
            label,
            options_with_placeholder,
            index=options_with_placeholder.index(current_value)
            if current_value in options_with_placeholder else 0,
            key=f"select_{label}"
        )

        st.session_state[label] = selected if selected != placeholder else ""







