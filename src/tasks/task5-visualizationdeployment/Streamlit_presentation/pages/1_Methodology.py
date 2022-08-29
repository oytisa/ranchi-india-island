import streamlit as st

st.header('Methodology')

st.markdown(
    """
    <style>
    .small-font {
        font-size:12px;
        font-style: italic;
        color: #b1a7a6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '''
    * Process Google Earth Engine (GEE) satellite images of Sagar Island to get water areas for the years 1990, 2000, 2010 and 2020.
    * Test few methods for automated shoreline detection
        * Method 1: GEE Otsu’s thresholding algorithm
        * Method 2: CoastSat module 
    * GEE generate shapefile of shorelines for the four years
    * Using ArcGIS and DSAS: 
        * Digitize shoreline more accurately to get accurate transects at select shoreline locations
        * Generat Transects along the digitized shoreline.
        * Compute end poit rate (EPR) linear regression rates (LRR) of change (erosion or accretion).
        * Predict future change in shoreline.  
    '''  
)