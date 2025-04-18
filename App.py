import streamlit as st
import ee
from google.oauth2.credentials import Credentials

st.set_page_config(page_title="GEE Init Test", layout="centered")
st.title("🌍 Google Earth Engine Initialization Test")

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
        return e

with st.spinner("Initializing Earth Engine..."):
    result = initialize_ee()

if result is True:
    st.success("✅ GEE is working!")
    st.write("🎉 Earth Engine has been successfully initialized using your refresh token.")
    
    # BONUS: print something from Earth Engine to prove it works
    image = ee.Image("COPERNICUS/S2_SR/20230401T160601_20230401T160601_T18TYN")
    st.write("Sample Earth Engine Image ID:")
    st.code(image.getInfo()["id"])
else:
    st.error("❌ Earth Engine initialization failed.")
    st.exception(result)
