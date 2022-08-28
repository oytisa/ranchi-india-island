import streamlit as st
import pandas as pd
import folium
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
sh1990 = geopandas.read_file('./coastal_shapefiles/Shoreline_1990.zip')
folium.GeoJson(data=sh1990["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'purple'}, name = '1990').add_to(sagar)

sh2000 = geopandas.read_file('./coastal_shapefiles/Shoreline_2000.zip')
folium.GeoJson(data=sh2000["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'red'}, name = '2000').add_to(sagar)


sh2010 = geopandas.read_file('./coastal_shapefiles/Shoreline_2010.zip')
folium.GeoJson(data=sh2010["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : 'blue'}, name = '2010').add_to(sagar)

sh2020 = geopandas.read_file('./coastal_shapefiles/Shoreline_2020.zip') 
folium.GeoJson(data=sh2020["geometry"], style_function = lambda x: {'fillColor' : 'none','color' : 'green'}, name = '2020').add_to(sagar)


path = './Transects_g/transects_n.zip'
gdf_o = geopandas.read_file(path)

gdf = gdf_o.copy()

#make classes and label them using cuts by change rate
gdf['LRR_cut'] = pd.cut(gdf['LRR'], bins = [-30, -20, -5, 0, 5, 20, 31], 
                                    labels = ['Large Erosion','Moderate Erosion', 'Low Erosion', 
                                    'Low Accretion', 'Medium Accretion', 'Large Accretion']) 
                                   
                                    
#Make color labels for                                    
color_dict = {
              'Large Erosion': '#ff0000', #red
              'Moderate Erosion': '#ff9933', #orange
              'Low Erosion': '#ffff00',  #yellow
              'Low Accretion': '#00cc66', #green 
              'Medium Accretion': '#3399ff', #blue 
              'Large Accretion': '#6600cc',  #purple 
              }
                                    
temp = gdf['LRR_cut'].map(color_dict)
gdf['LRR_color'] = temp.copy()

#examine what is in geojson file
#gdf.to_file('transects.geojson', driver = 'GeoJSON')


#Layer each group of Transects seperately
#First we create the dataframes 

gdf_erosion_low = gdf[gdf['LRR_cut'] == 'Low Erosion']
gdf_erosion_medium = gdf[gdf['LRR_cut'] == 'Moderate Erosion']
gdf_erosion_high = gdf[gdf['LRR_cut'] == 'Large Erosion']

gdf_accretion_low = gdf[gdf['LRR_cut'] == 'Low Accretion']
gdf_accretion_medium = gdf[gdf['LRR_cut'] == 'Medium Accretion']
gdf_accretion_high = gdf[gdf['LRR_cut'] == 'Large Accretion']


style_fun = lambda x: {'color': x['properties']['LRR_color']} 
folium.GeoJson(data = gdf_erosion_low[['geometry','LRR_color']], style_function = style_fun, name = 'Low Erosion: -5 < LRR < 0 ').add_to(sagar)
folium.GeoJson(data = gdf_erosion_medium[['geometry','LRR_color']], style_function = style_fun, name = 'Medium Erosion: -20 < LRR <-5 ').add_to(sagar)
folium.GeoJson(data = gdf_erosion_high[['geometry','LRR_color']], style_function = style_fun, name = 'High Erosion: -30 < LRR < -20 ').add_to(sagar)


folium.GeoJson(data = gdf_accretion_low[['geometry','LRR_color']], style_function = style_fun, name = 'Low Accretion: 0 < LRR < 5 ').add_to(sagar)#
folium.GeoJson(data = gdf_accretion_medium[['geometry','LRR_color']], style_function = style_fun, name = 'Medium Accretion: 5 < LRR < 20 ').add_to(sagar)
folium.GeoJson(data = gdf_accretion_high[['geometry','LRR_color']], style_function = style_fun, name = 'High Accretion: 20 < LRR < 31 ').add_to(sagar)


#predicted shorelines of 2030 and 2040
sh2030 = geopandas.read_file('./Transects_g/2030_pred.zip')
folium.GeoJson(data=sh2030["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : '#339933'}, name = '2030 prediction').add_to(sagar)

sh2040 = geopandas.read_file('./Transects_g/2040_pred.zip')
folium.GeoJson(data=sh2040["geometry"], style_function = lambda x: {'fillColor' : 'white','color' : '#003399'}, name = '2040 prediction').add_to(sagar)

#To choose the check on/off layers 
folium.map.LayerControl('topleft', collapsed= True).add_to(sagar)

#display map
sagar
