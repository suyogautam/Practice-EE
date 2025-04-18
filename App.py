import ee
import streamlit as st
import json

# Load credentials from secrets
creds = json.loads(st.secrets["EARTH_ENGINE_CREDENTIALS"])

# Manually initialize (alternative to ee.Initialize())
ee_token = ee.oauth.Token(
    creds["refresh_token"],
    creds["scopes"],
    creds["redirect_uri"]
)
ee.data.setToken(ee_token)
ee.Initialize()
