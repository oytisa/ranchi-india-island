import streamlit as st
import matplotlib.pyplot as plt

st.header('CoastSat Results')
st.write('Here we see the output of CoastSat shoreline detection applied to images of water-land classification by MNDWI')
st.markdown(
'''

Drawback: 

    * Does not save output as shapefile or geoJson format
    * shoreline outline detection not continuous 
'''
)