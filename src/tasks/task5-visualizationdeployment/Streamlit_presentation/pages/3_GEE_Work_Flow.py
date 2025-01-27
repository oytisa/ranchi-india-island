import streamlit as st

#path = "/app/ranchi-india-island"
st.header('Workflow in Google Earth Engine')
st.markdown(
'''
Below is a chart that shows our shoreline auto-dection method and shapefile generation
[code link](https://code.earthengine.google.com/?scriptPath=users%2Fhalajadallah%2FOmdena_india%3Acoastal_erosion_sagar)
'''
)  

st.image("data/gee_work_flow.PNG", width=800)
