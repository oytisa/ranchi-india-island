import streamlit as st
import matplotlib.pyplot as plt

st.header("CoastSat Results")
st.write("Here we see the output of CoastSat shoreline detection.")
st.markdown(
'''
The library applies image classification and sub-pixel resolution to MNDWI images along with OTSU's thresholding algorithm.
We found some difficulties. Firstly, we did not realise the package outputs a geojson file of multipoints of the shorelines it detects. 
Secondly, after the end of the project we came back it find the geojson file requires some processing for further use. In particulr, the points 
along the shoreline are quite dense.
'''
)
st.image("data/coastsat_output.PNG") 
