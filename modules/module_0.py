import os
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import seaborn as sns


class GUI:

    def __init__(self):
        self.uploaded_file = None
        if not os.path.exists('pickledir'):
            os.makedirs('pickledir')
        self.feature_to_display = []
        self.plot_3d_map_checkbox = False
        self.plot_2d_scatter_checkbox = False
        # filteration methods
        self.filter_ZS = False
        self.filter_LOF = False
        self.filter_IF = False

    def intro_gui(self):
        st.header('Section i: Introduction')
        st.markdown(open('README.md').read())

    def data_entry_gui(self):
        # st.header('Section ii: Data Entry')
        # uploaded file here is expected to be a xlsx file
        self.uploaded_file = st.file_uploader("Choose an input file (*.csv,*.xlsx,*.txt)")

    def header_gui(self, strng):
        st.header(strng)

    def subheader_gui(self, strng):
        st.subheader(strng)

    def feature_selection(self, df):
        self.feature_to_display = st.selectbox(
            "Feature to display:",
            tuple([df.columns[-1]] + list(df.columns[0:-1])), key='feature')

    def write(self, df):
        st.write(df)

    def filteration(self):
        self.write('choose outlier detection method(s):')
        self.filter_LOF = st.checkbox('Local Outlier Factor')
        self.filter_ZS = st.checkbox('Z score')
        self.filter_IF = st.checkbox('Isolation Forest')

    def plot_2d_scatter(self, df):
        self.plot_2d_scatter_checkbox = st.checkbox('scatter plot?', key=None)

        if self.plot_2d_scatter_checkbox:
            x = st.selectbox('Select x axis:', df.columns, key='x')
            y = st.selectbox('Select y axis:', df.columns, key='y')
            # y = st.selectbox('Select legend variable:', df.columns)
            sns.scatterplot(data=df, x=x, y=y)
            st.pyplot()

    def plot_3d_map(self, df):
        self.plot_3d_map_checkbox = st.checkbox('Is geographical data available?', key=None)

        if self.plot_3d_map_checkbox:
            # lng = st.selectbox('Select longitude:', df.columns)
            # lat = st.selectbox('Select latitude:', df.columns)
            # print("'"+lat+"'")
            pitch_ang = st.slider('3D plot pitch angle:', 0, 60, 40)
            # st.pydeck_chart(pdk.Deck(
            #     map_style='mapbox://styles/mapbox/light-v9',
            #     initial_view_state=pdk.ViewState(
            #         latitude=df[lat].mean(),
            #         longitude=df[lng].mean(),
            #         zoom=11,
            #         pitch=pitch_ang,
            #     ),
            #     layers=[
            #         pdk.Layer(
            #             'ColumnLayer',
            #             data=df,
            #             get_position=[lng, lat],
            #             get_elevation=self.feature_to_display,
            #             # get_fill_color=[100, feature_to_display*1, 100, 155],
            #             radius=200,
            #             elevation_scale=70,
            #             elevation_range=[0, 1000],
            #             pickable=True,
            #             extruded=True,
            #             get_color='[20, 300, 13, 160]',
            #             auto_highlight=True,
            #         ),
            #         pdk.Layer(
            #             'ScatterplotLayer',
            #             data=df,
            #             get_position=[lng, lat],
            #             get_elevation=self.feature_to_display,
            #             # get_fill_color=[150, feature_to_display*1, 150, 55],
            #             get_color='[20, 300, 13, 160]',
            #             get_radius=200,
            #             auto_highlight=True,
            #         ),
            #     ],
            # ))

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
                        get_elevation=self.feature_to_display,
                        # get_fill_color=[100, feature_to_display*1, 100, 155],
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
                        get_elevation=self.feature_to_display,
                        # get_fill_color=[150, feature_to_display*1, 150, 55],
                        get_color='[20, 300, 13, 160]',
                        get_radius=200,
                        auto_highlight=True,
                    ),
                ],
            ))

    def plot_histogram(self, df):
        # col1, col2, col3 = st.beta_columns(3)
        # with col1:
        st.header(self.feature_to_display)
        self.plot_histogram_checkbox = st.checkbox('Histogram plot?', key=None)
        if self.plot_histogram_checkbox:
            sns.histplot(df[[self.feature_to_display]], binwidth=5, kde=True)
            st.pyplot()

    def plot_2d_scatter_outlier(self, df, outlier_method):
        self.write('plot outliers with inliers:')
        x = st.selectbox('select horizontal axis:', df.columns, key='xx')
        y = st.selectbox('select vertical axis:', df.columns, key='yy')
        # outlier = st.multiselect('select outlier method to plot:', [], key='IF')
        colors = np.array(['#377eb8', '#ff7f00'])
        for out in outlier_method:
            self.write(' '.join(out.split('_')) + ':')
            fig, ax = plt.subplots()
            for idx, labels in [(0, 'inlier'), (1, 'outlier')]:
                sub_df = df[df[out] == idx]
                ax.scatter(sub_df[x], sub_df[y], s=20, label=labels,
                           color=colors[idx])
            fig.legend()
            st.pyplot()
