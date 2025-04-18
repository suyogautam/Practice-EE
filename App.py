import ee
import streamlit as st
from pathlib import Path

# Load token from Streamlit secrets
ee_token = st.secrets["EARTH_ENGINE_TOKEN"]

# Write the token to a temporary file (or mimic auth)
creds_file = Path.home() / ".config/earthengine/credentials"
creds_file.parent.mkdir(parents=True, exist_ok=True)
creds_file.write_text(ee_token)

# Initialize GEE
ee.Initialize()
