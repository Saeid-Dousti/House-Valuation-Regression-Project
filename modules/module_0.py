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

    def plot_3d_map(self, df):
        print(tuple(df.columns))

        # feature_to_displace = st.selectbox(
        #     "Feature to displace:",
        #     tuple(df.columns[1:])
        # )
        # print(f'{feature_to_displace}')

        # pitch_ang = st.slider('3D plot pitch angle:', 0, 60, 50)
        # st.pydeck_chart(pdk.Deck(
        #     map_style='mapbox://styles/mapbox/light-v9',
        #     initial_view_state=pdk.ViewState(
        #         latitude=df['X5_latitude'].mean(),
        #         longitude=df['X6_longitude'].mean(),
        #         zoom=11,
        #         pitch=pitch_ang,
        #     ),
        #     layers=[
        #         pdk.Layer(
        #             'HexagonLayer',
        #             data=df,
        #             get_position=['X6_longitude', 'X5_latitude'],
        #             get_elevation='Y_house_price_of_unit_area',
        #             radius=200,
        #             elevation_scale=7,
        #             elevation_range=[0, 1000],
        #             pickable=True,
        #             extruded=True,
        #         ),
        #         pdk.Layer(
        #             'ScatterplotLayer',
        #             data=df,
        #             get_position=['X6_longitude', 'X5_latitude'],
        #             get_elevation='Y_house_price_of_unit_area',
        #             get_color='[200, 30, 0, 160]',
        #             get_radius=200,
        #         ),
        #     ],
        # ))

        ####

        feature_to_displace = st.selectbox(
            "Feature to displace:",
            tuple(df.columns[1:])
        )
        pitch_ang = st.slider('3D plot pitch angle:', 0, 60, 40)
        # scale = st.slider('3D plot scale:', 0.0, 10.0, 5.0)
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=df['X5_latitude'].mean(),
                longitude=df['X6_longitude'].mean(),
                zoom=11,
                pitch=pitch_ang,
            ),
            layers=[
                pdk.Layer(
                    'ColumnLayer',
                    data=df,
                    get_position=['X6_longitude', 'X5_latitude'],
                    get_elevation=feature_to_displace,
                    # get_fill_color=[100, feature_to_displace*1, 100, 155],
                    radius=200,
                    elevation_scale=70,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                    get_color='[20, 300, 13, 160]',
                    auto_highlight=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position=['X6_longitude', 'X5_latitude'],
                    get_elevation=feature_to_displace,
                    # get_fill_color=[150, feature_to_displace*1, 150, 55],
                    get_color='[20, 300, 13, 160]',
                    get_radius=200,
                    auto_highlight=True,
                ),
            ],
        ))

        '''
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
                    get_elevation="Y house price of unit area",
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
                    get_elevation="Y house price of unit area",
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
        '''

        # DATA_URL = "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv"
        # df = pd.read_csv(DATA_URL)
        # print(df.head())
        # st.pydeck_chart(pdk.Deck(
        #     map_style='mapbox://styles/mapbox/light-v9',
        #     initial_view_state=pdk.ViewState(
        #         latitude=df['lat'].mean(),
        #         longitude=df['lng'].mean(),
        #         zoom=11,
        #         pitch=50,
        #     ),
        #     layers=[
        #         pdk.Layer(
        #             'HexagonLayer',
        #             data=df,
        #             get_position=["lng", "lat"],
        #             get_elevation="price_per_unit_area",
        #             radius=200,
        #             get_fill_color=["mrt_distance * 10", "mrt_distance", "mrt_distance * 10", 140],
        #             elevation_scale=6,
        #             elevation_range=[0, 1000],
        #             pickable=True,
        #             extruded=True,
        #         ),
        #         pdk.Layer(
        #             'ScatterplotLayer',
        #             data=df,
        #             get_position=["lng", "lat"],
        #             get_elevation="price_per_unit_area",
        #             get_color='[200, 30, 0, 160]',
        #             get_radius=200,
        #             get_fill_color=["mrt_distance * 10", "mrt_distance", "mrt_distance * 10", 140],
        #         ),
        #     ],
        # ))

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
