import os
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk


class GUI:

    def __init__(self):
        self.uploaded_file = None
        if not os.path.exists('pickledir'):
            os.makedirs('pickledir')

    def intro_gui(self):
        st.markdown(open('README.md').read())

    def data_entry_gui(self):
        st.header('Data Entry')
        # uploaded file here is expected to be a xlsx file
        self.uploaded_file = st.file_uploader("Choose an input file (*.csv,*.xlsx,*.txt)")
        # st.write(self.uploaded_file)
        # dataframe = pd.read_excel(self.uploaded_file)
        # st.write(dataframe)

    def table_df(self, dataframe):
        st.write(dataframe)

    def plot_map(self, df):
        print(df)
        DATA_URL = "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv"
        df = pd.read_csv(DATA_URL)
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=df['lat'].mean(),
                longitude=df['lng'].mean(),
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position=["lng", "lat"],
                    get_elevation="price_per_unit_area",
                    radius=200,
                    elevation_scale=6,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position=["lng", "lat"],
                    get_elevation="price_per_unit_area",
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
        ''':cvar
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=df['X5 latitude'].mean(),
                longitude=df['X6 longitude'].mean(),
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position=['X6 longitude', 'X5 latitude'],
                    get_elevation=['Y house price of unit area'],
                    radius=200,
                    elevation_scale=40,
                    elevation_range=[0, 10000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position=['X6 longitude', 'X5 latitude'],
                    get_elevation=['Y house price of unit area'],
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
        '''

        ''':cvar
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=37.76,
                longitude=-122.4,
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position='[lon, lat]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
        '''