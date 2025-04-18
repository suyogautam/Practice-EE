import streamlit as st
import ee
from google.oauth2.credentials import Credentials

@st.cache_resource
def initialize_ee():
    try:
        creds = Credentials(
            token=None,
            refresh_token=st.secrets["GEE_REFRESH_TOKEN"],
            token_uri="https://oauth2.googleapis.com/token",
            client_id=st.secrets["GEE_CLIENT_ID"],
            client_secret=st.secrets["GEE_CLIENT_SECRET"],
        )
        ee.Initialize(creds)
        return True
    except Exception as e:
        st.error(f"Earth Engine initialization failed: {e}")
        return False
