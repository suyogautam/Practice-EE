import streamlit as st
import ee
from google.oauth2.credentials import Credentials

st.set_page_config(page_title="GEE Test", layout="centered")
st.title("🌍 GEE Initialization Test")

try:
    @st.cache_resource
    def initialize_ee():
        creds = Credentials(
            token=None,
            refresh_token=st.secrets["GEE_REFRESH_TOKEN"],
            token_uri="https://oauth2.googleapis.com/token",
            client_id=st.secrets["GEE_CLIENT_ID"],
            client_secret=st.secrets["GEE_CLIENT_SECRET"],
        )
        ee.Initialize(creds)
        return True

    with st.spinner("Initializing Google Earth Engine..."):
        status = initialize_ee()

    if status is True:
        st.success("✅ Earth Engine initialized successfully!")
    else:
        st.error("❌ Earth Engine initialization failed.")
except Exception as e:
    st.error("⚠️ Unexpected error occurred.")
    st.exception(e)
