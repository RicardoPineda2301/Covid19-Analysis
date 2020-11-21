import streamlit as st
import pandas as pd
import numpy as np
from streamlit import cache
import altair as alt
import pydeck as pdk

df = pd.read_csv("proyecto/time_series_covid19_confirmed_global.csv").rename(columns= {'Lat': 'lat', 'Long': 'lon'})

data = df.melt(id_vars=['Province/State', 'Country/Region', 'lat', 'lon'], var_name='Fecha', value_name='Casos')
data['Fecha'] =  pd.to_datetime(data['Fecha'])

# Variables
DATE_TIME = "Fecha"


st.title("Casos de coronavirus")

hour_selected = st.date_input("Seleccione fecha",data['Fecha'].min(),  data['Fecha'].min(), data['Fecha'].max())

st.write(
    """Gráfica de casos de coronavirus en el mundo
    """)


    
mostrar = data[data[DATE_TIME] == hour_selected.isoformat()]



# Set viewport for the deckgl map
view = pdk.ViewState(latitude=0, longitude=0, zoom=0.2,)

# Create the scatter plot layer
covidLayer = pdk.Layer(
        "ScatterplotLayer",
        data=mostrar[['Casos', 'lat', 'lon']],
        pickable=False,
        opacity=0.3,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=5,
        radius_max_pixels=20,
        line_width_min_pixels=1,
        get_position=["lon", "lat"],
        get_radius='Casos',
        get_fill_color=[252, 136, 3],
        get_line_color=[255,0,0],
        tooltip="test test"
    )



# Create the deck.gl map
r = pdk.Deck(
    layers=[covidLayer],
    initial_view_state=view,
    map_style="mapbox://styles/mapbox/light-v10",
)


# Create a subheading to display current date
subheading = st.subheader("")

# Render the deck.gl map in the Streamlit app as a Pydeck chart 
map = st.pydeck_chart(r)

