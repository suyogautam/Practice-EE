import streamlit as st
import geemap
import ee
import json

# Set page configuration
st.set_page_config(page_title="GEE Test", layout="centered")

st.title("🌍 Google Earth Engine Initialization Test")

@st.cache_resource
def initialize_earth_engine():
    try:
        # Load service account credentials from Streamlit secrets
        service_account = st.secrets["GEE_SERVICE_ACCOUNT"]
        key_json = json.loads(st.secrets["GEE_SERVICE_KEY"])

        credentials = ee.ServiceAccountCredentials(service_account, key_data=key_json)
        ee.Initialize(credentials)

        return "✅ Earth Engine initialized successfully!"
    except Exception as e:
        return f"❌ Earth Engine initialization failed: {e}"

# Initialize EE and display the result
with st.spinner("Initializing Google Earth Engine..."):
    result = initialize_earth_engine()

st.success(result) if result.startswith("✅") else st.error(result)
