import streamlit as st
from modules.module_0 import GUI
from modules.module_1 import Reg_Data
from modules.module_2 import DataFiltering


# section_zero, pars_arg, , \
#     section_one, section_two, section_three, section_four, \
#     section_five


def main():
    # tb._SYMBOLIC_SCOPE.value = True

    intro_butt = st.sidebar.checkbox('1) Introduction', key=None)

    gui = GUI()

    if intro_butt:
        # gui.header_gui('Section i: Introduction')
        gui.intro_gui()

    data_but = st.sidebar.checkbox('2) Data Entry', key=None)

    if data_but:
        gui.header_gui('Section ii): Data Entry')
        gui.data_entry_gui()
        data = Reg_Data(gui.uploaded_file)
        gui.feature_selection(data.raw_data)
        gui.write(data.raw_data)
        gui.plot_3d_map(data.raw_data)
        # st.success('This is a success message!')
        gui.plot_histogram(data.raw_data)
        gui.plot_2d_scatter(data.raw_data)

    data_filter = st.sidebar.checkbox('3) Data Filtering', key=None)

    # section iii)
    gui.header_gui('Section iii: Data Filtering')
    ## a) outlier detection:
    st.subheader('a) outlier detection:')

    if data_filter:

        data_filtering = DataFiltering()

        # this will remove the index column
        gui.write('Remove "No" column which is redundant:')
        data.drop_index()  # dropping the No column which is redundant in our df
        gui.write(data.no_index_data)
        # gui.write(data.no_index_data.columns)
        gui.filteration()  # show the outlier dection options
        # gui.filter_ZS
        # gui.filter_LOF
        # gui.filter_IF
        data.outlier_data = data.no_index_data.copy(deep=True)  # data frame with outlier detected column

        outlier_method = []

        if gui.filter_LOF:
            data.outlier_data = data_filtering.local_outlier_factor(data.outlier_data)
            outlier_method.append('LOF_outlier')

        if gui.filter_ZS:
            data.outlier_data = data_filtering.z_score(data.outlier_data)
            outlier_method.append('ZScore_outlier')

        if gui.filter_IF:
            data.outlier_data = data_filtering.isolation_forest(data.outlier_data)
            outlier_method.append('IF_outlier')

        data_filtering.outlier_method = outlier_method # specifies the outlier methods used by the user

        gui.write('In the following table 0: inlier, 1:outlier')
        gui.write(data.outlier_data)

        gui.plot_2d_scatter_outlier(data.outlier_data, outlier_method)

        gui.subheader_gui('b) interpolation:')

        ## b) interpolation:
        '''
            two approaches for interpolation technique: 
                - create a new grid with more points for each feature
                - replace the outliers with interpolated values
        '''

        data.corrected_data = data_filtering.interpolation(data.outlier_data)


if __name__ == '__main__':
    main()
