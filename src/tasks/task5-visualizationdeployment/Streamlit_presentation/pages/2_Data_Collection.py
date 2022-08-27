import pandas as pd
import numpy as np
import streamlit as st
import os

path = os.getcwd()
st.write('path ',path)
file_path = os.join(path,'landsat_images_ids.csv')

st.write('file_path',file_path)

df = pd.read_csv(file_path)

st.header('Data Collection')
st.markdown(
'''
Landasat  Level 2 Surface Reflectence Data was collected using Google Earth Engine

Below is a list of image IDs
'''
)

st.write(df)