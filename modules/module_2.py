import numpy as np
import streamlit as st
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from scipy.interpolate import interpolate


class DataFiltering:

    def __init__(self):
        self.mask_local_outlier_factor = None
        self.outlier_method = []

    def local_outlier_factor(self, df):
        # df = df.copy(deep=True)
        st.write('Local Outlier Factor Method:')
        neighbors = st.slider('select number of neighbors for outlier detection:', 1, len(df) // 10,
                              max(2, len(df) // 20))

        features = st.multiselect('select the features for outlier detection:', df.columns, key='LOF')
        if not features:
            return
        clf = LocalOutlierFactor(n_neighbors=neighbors)
        # clf.fit_predict(df) predicts outliers as -1 and inliers as 1
        # print(df.iloc[:, 6:])
        self.mask_local_outlier_factor = (-1 * clf.fit_predict(df[features]) + 1) // 2
        # print(list(map(bool, self.mask_local_outlier_factor)))
        # df['LOF_outlier'] = list(map(bool, self.mask_local_outlier_factor))
        df['LOF_outlier'] = self.mask_local_outlier_factor

        return df

    def z_score(self, df):
        # df = df.copy(deep=True)
        st.write('Z Score Method (based on threshold=3):')
        feature = st.selectbox('select a feature for outlier detection:', df.columns)

        threshold = 3

        df['ZScore_outlier'] = df[feature].apply(
            lambda x: int(abs(x - df[feature].mean()) / df[feature].std() > threshold))
        # df.columns
        return df

    def isolation_forest(self, df):
        # df = df.copy(deep=True)
        st.write('Isolation forest method:')
        outliers_fraction = st.slider('select outlier fraction for isolation forest:', 0.001, 0.3, 0.01)
        features = st.multiselect('select the features for outlier detection:', df.columns, key='IF')
        clf = IsolationForest(contamination=outliers_fraction, random_state=42)

        self.mask_local_outlier_factor = (-1 * clf.fit(df[features]).predict(df[features]) + 1) // 2
        df['IF_outlier'] = self.mask_local_outlier_factor

        return df

    def interpolation(self, df):

        df = df.copy(deep=True)

        output_variable = st.selectbox(
            'select the variable to be corrected (should match w/ outlier detection feature):', df.columns,
            key='output')

        indep_variable = st.selectbox('select the independent variable to interpolate with:', df.columns,
                                      key='independent')

        outliers_correction = st.selectbox('select outliers detected method:',
                                           self.outlier_method)

        df_no_outlier = df[df[outliers_correction] == 0]

        df_only_outlier = df[df[outliers_correction] == 1]

        st.write(df_no_outlier)

        interp_method = st.selectbox('select the interpolation method:',
                                     ['linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic'])

        if interp_method in ['quadratic', 'cubic']:
            st.write('warning: for this interpolation algorithm, the independent variables should be stricktly ascending!')
            df_no_outlier.sort_values(by=[indep_variable], inplace=True)
            # print(np.array(df_no_outlier[indep_variable]))
            # print(np.array(df_no_outlier[indep_variable]).ndim)
            # print(np.any(np.array(df_no_outlier[indep_variable])[1:] < np.array(df_no_outlier[indep_variable])[:-1]))

            f = interpolate.interp1d(np.array(df_no_outlier[indep_variable]), np.array(df_no_outlier[output_variable]),
                                     kind=interp_method, bounds_error=False,
                                     fill_value=df_no_outlier[output_variable].mean())
        else:
            f = interpolate.interp1d(np.array(df_no_outlier[indep_variable]), np.array(df_no_outlier[output_variable]),
                                     kind=interp_method, bounds_error=False,
                                     fill_value=df_no_outlier[output_variable].mean())

        df[output_variable][df[outliers_correction] == 1] = np.array(f(df_only_outlier[indep_variable]))

        st.write('The interpolated outliers:')

        st.write(df[df[outliers_correction] == 1])

        return df
