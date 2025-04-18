import ee
import streamlit as st
import json
import os
from pathlib import Path

# Initialize Earth Engine
def initialize_ee():
    try:
        # Method 1: Try normal initialization (works if ee.Authenticate() was run locally)
        ee.Initialize()
        st.success("Earth Engine initialized successfully!")
    except Exception as e:
        st.warning("Standard initialization failed. Trying alternative methods...")
        
        try:
            # Method 2: Use credentials from Streamlit secrets
            if 'EARTH_ENGINE_CREDENTIALS' in st.secrets:
                creds = json.loads(st.secrets["EARTH_ENGINE_CREDENTIALS"])
                
                # Create the credentials file in the expected location
                creds_dir = Path.home() / ".config/earthengine"
                creds_dir.mkdir(parents=True, exist_ok=True)
                (creds_dir / "credentials").write_text(json.dumps(creds))
                
                ee.Initialize()
                st.success("Initialized using Streamlit secrets!")
            else:
                st.error("No Earth Engine credentials found in secrets")
        except Exception as e:
            st.error(f"Failed to initialize Earth Engine: {str(e)}")
            st.info("For local development, run 'earthengine authenticate' in your terminal.")

# Call the initialization function
initialize_ee()

# Your app code continues here...
st.title("Earth Engine App")
