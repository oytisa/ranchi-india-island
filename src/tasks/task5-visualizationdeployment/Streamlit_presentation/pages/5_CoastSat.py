import streamlit as st
import matplotlib.pyplot as plt

st.header("CoastSat Results")
st.write("Here we see the output of CoastSat shoreline detection.")
st.markdown(
'''
The library applies image classification and sub-pixel resolution to MNDWI images along with OTSU's thresholding algorithm.
'''
)
st.image("data/coastsat_output.PNG") 
