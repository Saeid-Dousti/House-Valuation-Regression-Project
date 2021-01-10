import os
import streamlit as st
import pandas as pd
import numpy as np


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
