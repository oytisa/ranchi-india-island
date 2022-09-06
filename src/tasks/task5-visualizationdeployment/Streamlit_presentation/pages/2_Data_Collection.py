import pandas as pd
import numpy as np
import streamlit as st
import os

print(os.system('pwd'))
#print(os.system('ls -lrt /app/ranchi-india-island/src/tasks/task5-visualizationdeployment/Streamlit_presentation/data'))

#file_path = '/app/ranchi-india-island/src/tasks/task5-visualizationdeployment/Streamlit_presentation/data/landsat_images_ids.csv'
file_path = 'data/landsat_images_ids.csv'
df = pd.read_csv(file_path)

st.header('Data Collection')
st.markdown(
'''
Landasat  Level 2 Surface Reflectence Data was collected using Google Earth Engine with cloud cover less than 10%. This is most likely in the months of November and December. 

Below is a list of image IDs
'''
)

st.write(df)
