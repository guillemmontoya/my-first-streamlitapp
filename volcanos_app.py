import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

#Load volcanos dataframe and create a copy from it
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

volcanos_df_raw = load_data(path="./data/volcano_ds_pop.csv")
volcanos_df = deepcopy(volcanos_df_raw)

volcanos_df['Country'] = volcanos_df['Country'].replace({'United States':'United States of America',
                                                                      'Tanzania':'United Republic of Tanzania',
                                                                      'Martinique':'Martinique',
                                                                      'Sao Tome & Principe':'Sao Tome and Principe',
                                                                      'Guadeloupe':'Guadeloupe',
                                                                      'Wallis & Futuna':'Wallis and Futuna'})

# Add title and header
st.title("Introduction to Streamlit")
st.header("Volcanos Data Exploration")

if st.sidebar.checkbox("Show Dataframe"):
    st.subheader("That is the volcanos Dataframe")
    st.dataframe(data=volcanos_df)

left_column, middle_left_column, middle, right_column = st.columns([1, 2, 1, 2])

#Filtering height volcanos
air_volcanos = volcanos_df[volcanos_df['Elev'] > 0]

#First SELECT BOX
countries = ['All']+sorted(pd.unique(volcanos_df['Country']))
elev_volcanos = left_column.selectbox("Choose Height: ", ['All', '+6000m', '+5000m', '+4000m', '+3000m', '+2000m', '+1000m', '+100m'])

#Second SELECT BOX
statuses = ["All"]+sorted(pd.unique(volcanos_df['Status']))
statuses.remove('Hydrophonic')
statuses.remove('Seismicity')
status_volcanos = middle_left_column.selectbox("Choose Status of the volcanos: ", statuses)




#Filtering of the SELECT BOX
if elev_volcanos == "All":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 0]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 0) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+6000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 6000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 6000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+5000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 5000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 5000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+4000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 4000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 4000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+3000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 3000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 3000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+2000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 2000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 2000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+1000m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 1000]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 1000) & (air_volcanos['Status'] == 'Varve Count')]
elif elev_volcanos == "+100m":
    if status_volcanos == "All":
        volcanos_df_reduced = air_volcanos[air_volcanos["Elev"] >= 100]
    elif status_volcanos == "Anthropology":
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Anthropology')]
    elif status_volcanos == 'Ar/Ar':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Ar/Ar')]
    elif status_volcanos == 'Dendrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Dendrochronology')]
    elif status_volcanos == 'Fumarolic':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Fumarolic')]
    elif status_volcanos == 'Historical':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Historical')]
    elif status_volcanos == 'Holocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Holocene')]
    elif status_volcanos == 'Hot Springs':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Hot Springs')] 
    elif status_volcanos == 'Hydration Rind':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Hydration Rind')]
    elif status_volcanos == 'Pleistocene':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Pleistocene')]
    elif status_volcanos == 'Pleistocene-Fumarol':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Pleistocene-Fumarol')]
    elif status_volcanos == 'Radiocarbon':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Radiocarbon')]
    elif status_volcanos == 'Tephrochronology':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Tephrochronology')]
    elif status_volcanos == 'Uncertain':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Uncertain')]
    elif status_volcanos == 'Varve Count':
        volcanos_df_reduced = air_volcanos[(air_volcanos["Elev"] >= 100) & (air_volcanos['Status'] == 'Varve Count')]

#hydration rind, hydrophonic, sesmicity

#PLOTLY - VOLCANOS AROUND THE WORLD
fig2 = px.scatter_mapbox(
    volcanos_df_reduced,
    lat='Latitude', 
    lon='Longitude',
    color='Type',
    hover_name='Volcano Name',
    size='Elev',
    zoom=1,
    size_max=12
)


fig2.update_layout(
    mapbox_style='open-street-map', 
    mapbox_center={'lat': 0, 'lon': 0},
    width=920,
    height=800,
    title='Volcanos around the world',
    title_font_size=25,
    title_x=0.25
)
st.plotly_chart(fig2)


left_column2, middle_left_column2, middle2, right_column2 = st.columns([3, 1, 1, 1])

#Third RADIO BUTTON
radio_submarine = left_column2.radio("Do you want to see the Submarine Volcanos plot?", ['Yes', 'No'])

#Filtering submarine volcanos
submarine_volcanos = volcanos_df[volcanos_df['Elev'] < 0]


# PLOTLY - SUBMARINE VOLCANOS
fig4 = px.scatter_mapbox(
    submarine_volcanos,
    lat='Latitude', 
    lon='Longitude',  
    hover_name='Volcano Name',  
    zoom=1,
    color='Status',
    size=list(submarine_volcanos['Elev'].abs()),
    animation_group='Status',
    size_max=12
)


fig4.update_layout(
    mapbox_style='open-street-map', 
    mapbox_center={'lat': 0, 'lon': 0},
    width=920,
    height=800,
    title='Submarine volcanoes',
    title_font_size=25,
    title_x = 0.25
)

if radio_submarine == "Yes":
    st.plotly_chart(fig4)

st.subheader("A little bit more information regarding worldwide volcanos")

left_column4, middle4, right_column4 = st.columns([4, 1, 1])
mean_appears = left_column4.radio("Display mean elevation per type or amount of volcanos per type and status", ['Mean', 'Count'])

df10 = volcanos_df.groupby('Type', as_index=False).agg({'Elev':'mean'}).sort_values(by='Elev', ascending=False)
df10 = df10.rename(columns={'Elev':'Mean height'})


#PLOT 3
df6 = volcanos_df.groupby(['Type','Status'], as_index=False).agg({'Elev': 'count'})
df6 = df6.rename(columns={'Elev': 'Count'})
df6 = df6.sort_values(by='Count', ascending=False)

fig6 = px.bar(df6, x='Type', y='Count', color='Status')

if mean_appears == 'Mean':
    fig6 = px.scatter(df10, x='Type', y='Mean height')


fig6.update_layout(
    title_text = 'Information per volcano type',
    title_font_size=25,
    title_x=0.25,
    width=920,
    height=600

)
st.plotly_chart(fig6)




df7 = volcanos_df.groupby('Country', as_index=False).agg({'Elev': 'max'})
df7 = df7.sort_values(by='Elev', ascending=False)

country_name = []
elev_amount = []
volcano_name = []

for i,j in zip(df7['Country'], df7['Elev']):
    country_name.append(volcanos_df[(volcanos_df['Country'] == i) & (volcanos_df['Elev'] == j)]['Country'].values)
    elev_amount.append(volcanos_df[(volcanos_df['Country'] == i) & (volcanos_df['Elev'] == j)]['Elev'].values)
    volcano_name.append(volcanos_df[(volcanos_df['Country'] == i) & (volcanos_df['Elev'] == j)]['Volcano Name'].values)

country_list = []
for i in country_name:
    country_list.append(i[0])

elev_amount_list = []
for i in elev_amount:
    elev_amount_list.append(i[0])

name_list = []
for i in volcano_name:
    name_list.append(i[0])

data = {'Country Name':country_list, 'Elev':elev_amount_list, 'Volcano Name':name_list}
df8 = pd.DataFrame(data)

european_countries = ['Spain', 'Italy', 'Georgia', 'Portugal', 'Iceland', 'France', 'Sweden', 'Germany', 'Greece',
                      'Netherlands', 'United Kingdom']
oceania_countries = ['Papua New Guinea', 'Australia', 'New Zealand', 'Wallis and Futuna', 'Vanuatu', 'Guadeloupe',
                     'American Samoa', 'Fiji', 'Samoa', 'Tonga', 'Kiribati']
american_countries = ['Argentina', 'Peru', 'Ecuador', 'Chile', 'Bolivia', 'United States of America', 'Mexico',
                      'Guatemala', 'Colombia', 'Panama', 'Costa Rica', 'Canada', 'Honduras', 'Dominica', 'Martinique',
                      'South Africa', 'Montserrat', 'Grenada', 'United States of America', 'Honduras', 'Nicaragua',
                      'El Salvador']
asian_countries = ['China', 'Iran', 'Russia', 'Turkey', 'Afghanistan', 'Japan', 'Yemen', 'Saudi Arabia', 'South Korea',
                   'Myanmar', 'Indonesia', 'Philippines', 'India', 'Malaysia', 'Taiwan', 'Syria', 'Vietnam']
african_countries = ['United Republic of Tanzania', 'Cameroon', 'Rwanda', 'Chad', 'Sudan', 'Equatorial Guinea', 'Algeria',
                     'Madagascar', 'Kenya', 'North Korea', 'Ethiopia', 'Mongolia', 'Comoros', 'Eritrea', 'Djibouti',
                     'Sao Tome and Principe', 'Libya', 'South Africa', 'Nigeria']

country_continent_mapping = {}

for country in european_countries:
    country_continent_mapping[country] = 'Europe'

for country in oceania_countries:
    country_continent_mapping[country] = 'Oceania'

for country in american_countries:
    country_continent_mapping[country] = 'Americas'

for country in asian_countries:
    country_continent_mapping[country] = 'Asia'

for country in african_countries:
    country_continent_mapping[country] = 'Africa'

df8['Continent'] = df8['Country Name'].map(country_continent_mapping)

left_column3, middle_left_column3, middle3, right_column3 = st.columns([1, 1, 1, 1])

different_continents = left_column3.selectbox("Choose Continent: ", ['All', 'Americas', 'Africa', 'Asia', 'Europe', 'Oceania'])

df9 = deepcopy(df8)

if different_continents == 'All':
    df9 = df8
elif different_continents == 'Americas':
    df9 = df8[df8['Continent'] == 'Americas']
elif different_continents == "Africa":
    df9 = df8[df8['Continent'] == 'Africa']
elif different_continents == "Asia":
    df9 = df8[df8['Continent'] == 'Asia']
elif different_continents == "Europe":
    df9 = df8[df8['Continent'] == 'Europe']
elif different_continents == "Oceania":
    df9 = df8[df8['Continent'] == 'Oceania']


# PLOT 4
fig8 = px.scatter(df9, x='Country Name', y='Elev', color='Continent', hover_data={'Volcano Name':True}, range_y=[-100,8000])

fig8.update_layout(
    title_text = 'Highest volcanos per Country',
    title_font_size = 25,
    title_x=0.25,
    width=900
)
fig8.update_xaxes(categoryorder='total descending')
st.plotly_chart(fig8)