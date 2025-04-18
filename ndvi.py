import ee
import streamlit as st
import geemap.foliumap as geemap
import pandas as pd

# Title
st.title("MODIS NDVI Analysis (2024)")

# Initialize Earth Engine
try:
    ee.Initialize()
    st.success("Google Earth Engine initialized successfully!")
except Exception as e:
    st.error(f"Earth Engine initialization failed. Run **'earthengine authenticate'** in your terminal first.\nError: {e}")
    st.stop()

# Define NDVI calculation function
def calculate_mean_ndvi():
    # Load MODIS NDVI data (MOD13A2, 1km resolution)
    modis = ee.ImageCollection("MODIS/006/MOD13A2") \
             .filterDate('2024-01-01', '2024-12-31') \
             .select('NDVI')

    # Calculate mean NDVI for 2024
    mean_ndvi = modis.mean().multiply(0.0001)  # Scale factor (MODIS NDVI is scaled by 10,000)

    # Get mean NDVI value for the entire image
    stats = mean_ndvi.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=ee.Geometry.Rectangle([-180, -60, 180, 85]),  # Global (excluding Antarctica)
        scale=1000  # MODIS resolution
    ).getInfo()

    return mean_ndvi, stats

# Calculate and display results
mean_ndvi, stats = calculate_mean_ndvi()

# Show mean NDVI value
st.subheader("Results")
st.write(f"**Global Mean NDVI (2024):** {stats['NDVI']:.3f}")

# Display the NDVI map
st.subheader("NDVI Map (2024 Mean)")
Map = geemap.Map(center=[20, 0], zoom=2)
Map.addLayer(mean_ndvi, {'min': 0, 'max': 1, 'palette': ['red', 'yellow', 'green']}, 'NDVI')
Map.to_streamlit()

# Optional: Show pixel values on click
st.subheader("Pixel Inspector")
st.info("Click on the map above to see NDVI values at specific locations.")
Map.add_inspector_handles()