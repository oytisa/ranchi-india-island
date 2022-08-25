import streamlit as st
import pandas as pd
import folium
import numpy as np
import geopandas 


st.set_page_config(page_title='Shoreline Change Rate', layout = 'wide')

st.header('Shoreline Change')
st.subheader('Shorelines for each year: GEE workflow output')
st.subheader('Rate of Change : Linear Regression Rate (LRR) ArchGIS DSAS output')

#sagar is the base map
sagar = folium.Map(location = [ 21.72321,88.11324],zoom_start = 11, width = 1000, hight = 700 ) #tiles = 'openstreetmap', tiles = 'stamenterrain', tiles = 'Stamen Toner'
folium.TileLayer('openstreetmap').add_to(sagar)
folium.TileLayer('Stamen Toner').add_to(sagar)

#load shapefiles for 1990, 2000, 2010 and 2020
sh1990 = geopandas.read_file('./coastal_shapefiles/1990_sh.zip')
folium.GeoJson(data=sh1990["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'purple'}, name = '1990').add_to(sagar)

sh2000 = geopandas.read_file('./coastal_shapefiles/2000_sh.zip')
folium.GeoJson(data=sh2000["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'red'}, name = '2000').add_to(sagar)


sh2010 = geopandas.read_file('./coastal_shapefiles/2010_sh.zip')
folium.GeoJson(data=sh2010["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'blue'}, name = '2010').add_to(sagar)

sh2020 = geopandas.read_file('./coastal_shapefiles/2020_sh.zip')
folium.GeoJson(data=sh2020["geometry"], style_function = lambda x: {'fillColor' : 'none','color' : 'green'}, name = '2020').add_to(sagar)


path = './Transects_g/Transects.shp'
gdf = geopandas.read_file(path)

gdf_o = gdf
gdf = gdf_o[8:] #the first 8 entries are NANs
#make classes and label them using cuts by change rate
gdf['LRR_cut'] = pd.cut(gdf['LRR'], bins = [-53, -35, -20, -10, 0, 10, 20, 30, 40], 
                                    labels = ['Sever Erosion', 'Large Erosion','Moderate Erosion', 'Low Erosion', 'Low Accretion', 'Medium Accretion', 'Large Accretion', 
                                    'Extreme Accretion'])
                                    
#Make color labels for                                    
color_dict = {'Sever Erosion': '#800000', #maroon/brown
              'Large Erosion': '#ff0000', #red
              'Moderate Erosion': '#ff9933', #orange
              'Low Erosion': '#ffff00',  #yellow
              'Low Accretion': '#00cc66', #green 
              'Medium Accretion': '#3399ff', #blue 
              'Large Accretion': '#6600cc',  #purple 
              'Extreme Accretion': '#000000' #black 
              }
                                    
gdf['LRR_color'] = gdf['LRR_cut'].map(color_dict)

#examine what is in geojson file
#gdf.to_file('transects.geojson', driver = 'GeoJSON')

'''
Layer each group of Transects seperately
First we create the dataframes 
'''
gdf_erosion_low = gdf[gdf['LRR_cut'] == 'Low Erosion']
gdf_erosion_medium = gdf[gdf['LRR_cut'] == 'Moderate Erosion']
gdf_erosion_high = gdf[gdf['LRR_cut'] == 'Large Erosion']
gdf_erosion_extr = gdf[gdf['LRR_cut'] == 'Sever Erosion']

gdf_accretion_low = gdf[gdf['LRR_cut'] == 'Low Accretion']
gdf_accretion_medium = gdf[gdf['LRR_cut'] == 'Medium Accretion']
gdf_accretion_high = gdf[gdf['LRR_cut'] == 'Large Accretion']
gdf_accretion_extr = gdf[gdf['LRR_cut'] == 'Extreme Accretion']


style_fun = lambda x: {'color': x['properties']['LRR_color']} 
folium.GeoJson(data = gdf_erosion_low[['geometry','LRR_color']], style_function = style_fun, name = 'Low Erosion: -10 < LRR < 0 ').add_to(sagar)
folium.GeoJson(data = gdf_erosion_medium[['geometry','LRR_color']], style_function = style_fun, name = 'Medium Erosion: -20 < LRR <-10 ').add_to(sagar)
folium.GeoJson(data = gdf_erosion_high[['geometry','LRR_color']], style_function = style_fun, name = 'High Erosion: -35 < LRR < -20 ').add_to(sagar)
folium.GeoJson(data = gdf_erosion_extr[['geometry','LRR_color']], style_function = style_fun, name = 'Extreme Erosion: -53 < LRR < -35 ').add_to(sagar)

folium.GeoJson(data = gdf_accretion_low[['geometry','LRR_color']], style_function = style_fun, name = 'Low Accretion: 0 < LRR < 10 ').add_to(sagar)
folium.GeoJson(data = gdf_accretion_medium[['geometry','LRR_color']], style_function = style_fun, name = 'Medium Accretion: 10 < LRR < 20 ').add_to(sagar)
folium.GeoJson(data = gdf_accretion_high[['geometry','LRR_color']], style_function = style_fun, name = 'High Accretion: 20 < LRR < 30 ').add_to(sagar)
folium.GeoJson(data = gdf_accretion_extr[['geometry','LRR_color']], style_function = style_fun, name = 'Exteme Accretion: 30 < LRR < 40 ').add_to(sagar)

#To choose the check on/off layers 
folium.map.LayerControl('topleft', collapsed= True).add_to(sagar)

#display map
sagar