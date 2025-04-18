import ee
import streamlit as st
import geemap.foliumap as geemap

# Set up the Streamlit app
st.title("Google Earth Engine + Streamlit Demo")

# Initialize GEE
try:
    ee.Initialize()
except:
    st.error("GEE not authenticated. Please follow instructions above.")
    st.stop()

# Load a GEE dataset (e.g., NDVI)
dataset = ee.ImageCollection("MODIS/006/MOD13A2").filterDate('2020-01-01', '2021-01-01')
ndvi = dataset.select('NDVI').median()

# Center the map (e.g., over India)
Map = geemap.Map(center=[20.59, 78.96], zoom=5)
Map.addLayer(ndvi, {'min': 0, 'max': 9000, 'palette': ['red', 'yellow', 'green']}, 'NDVI')

# Display the map in Streamlit
Map.to_streamlit()
