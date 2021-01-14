import numpy as np
import streamlit as st
from sklearn.neighbors import LocalOutlierFactor


class DataFiltering:

    def __init__(self):
        self.mask_local_outlier_factor = None

    def local_outlier_factor(self, df):
        neighbors = st.slider('select number of neighbors for outlier detection:', 1, len(df) // 10,
                              max(2, len(df) // 20))

        clf = LocalOutlierFactor(n_neighbors=neighbors)
        # clf.fit_predict(df) predicts outliers as -1 and inliers as 1
        self.mask_local_outlier_factor = (-1 * clf.fit_predict(df) + 1) // 2
        # print(list(map(bool, self.mask_local_outlier_factor)))
        df['LOF_outlier'] = list(map(bool, self.mask_local_outlier_factor))

        return df


