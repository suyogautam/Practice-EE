import streamlit as st
import ee
import geemap.foliumap as geemap
import os

st.title("Google Earth Engine Authentication Test")

# Path to your credentials file
credentials_path = r"C:\Users\suyog\.config\earthengine\credentials"

try:
    # Initialize Earth Engine using the default credentials
    # This should automatically look for credentials in the default location
    ee.Initialize()
    st.success("✅ Authentication successful! You are connected to Google Earth Engine.")
    
    # Create a map centered on a location
    map_center = [0, 0]
    zoom_level = 2
    
    # Create a map object
    m = geemap.Map(center=map_center, zoom=zoom_level)
    
    # Add a simple Earth Engine layer - global SRTM elevation
    dem = ee.Image('USGS/SRTMGL1_003')
    vis_params = {
        'min': 0,
        'max': 4000,
        'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    }
    m.add_layer(dem, vis_params, 'SRTM DEM')
    
    # Display the map
    st.write("Simple Earth Engine map (showing global elevation):")
    m.to_streamlit(height=600)
    
    # Show some basic Earth Engine info to verify
    st.subheader("GEE Info:")
    info = ee.Image('USGS/SRTMGL1_003').getInfo()
    st.write(f"Image ID: {info['id']}")
    st.write(f"Type: {info['type']}")
    st.write(f"Bands: {[band['id'] for band in info['bands']]}")
    
except Exception as e:
    st.error(f"❌ Authentication failed with error: {str(e)}")
    st.info("Check your credentials and ensure GEE is properly configured.")
    
    # If authentication fails, provide more debugging info
    if os.path.exists(credentials_path):
        st.info(f"✓ Credentials file exists at {credentials_path}")
    else:
        st.error(f"✗ Credentials file not found at {credentials_path}")
