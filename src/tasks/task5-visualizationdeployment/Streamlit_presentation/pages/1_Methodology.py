import streamlit as st

st.header('Methodology')
st.markdown(
'''
* Process Google Earth Engine satellite images of Sagar Island to get water areas for the years 1990, 2000, 2010 and 2020.
* Test few methods for automated shoreline detection
    * Method 1: GEE Otsu’s thresholding algorithm
    * Method 2: CoastSat module 
* Generate shapefile of shorelines for the four years
* Using ArcGIS and DSAS, digitize shoreline more accurately to get accurate transects at select shoreline locations
* DSAS should genrate linear regression rates of change (erosion or accretion).
* Predict future change in shoreline.  

'''
)