import streamlit as st
from modules.module_0 import GUI
from modules.module_1 import Reg_Data
from modules.module_2 import DataFiltering
# section_zero, pars_arg, , \
#     section_one, section_two, section_three, section_four, \
#     section_five


def main():
    #tb._SYMBOLIC_SCOPE.value = True

    intro_butt = st.sidebar.checkbox('1) Introduction', key=None)

    gui = GUI()

    if intro_butt:
        gui.intro_gui()

    data_but = st.sidebar.checkbox('2) Data Entry', key=None)

    if data_but:
        gui.data_entry_gui()
        data = Reg_Data(gui.uploaded_file)
        gui.feature_selection(data.raw_data)
        gui.table_df(data.raw_data)
        gui.plot_3d_map(data.raw_data)
        # st.success('This is a success message!')
        gui.plot_histogram(data.raw_data)
        gui.plot_2d_scatter(data.raw_data)

    data_filter = st.sidebar.checkbox('3) Data Filtering', key=None)

    if data_filter:
        gui.data_filtering_gui()
        data_filtering = DataFiltering()

        # this will remove the index column
        st.write('Remove No column:')
        data.drop_index()
        gui.table_df(data.no_index_data)

        data.outlier_data = data_filtering.local_outlier_factor(data.no_index_data)

        gui.table_df(data.outlier_data)


if __name__ == '__main__':
    main()