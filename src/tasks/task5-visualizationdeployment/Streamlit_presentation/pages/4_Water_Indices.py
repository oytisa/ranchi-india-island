import streamlit as st


st.header('Water Indices')

st.markdown(
'''
To find shorelines we look for a water index that seperates water from land.

We explored the following two:

* Modified Normalized Difference Water Index (MNDWI) uses the green band and the first shortwave infrared (SWIR1) band
    
    * MNDWI = (Green - SWIR1)/(Green + SWIR1)
    
* Automated Water Extraction Index (AWEI) is a multispectral index, inadditioin to the green and SWIR1, uses  near infrared (NIR) and the second shortwave infrared (SWIR2) bands

    * AWEI = 4 * (Green - SWIR1) - (0.25 * NIR + 2.75 * SWIR2)
    

'''
)

