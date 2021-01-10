import streamlit as st
from modules.module_0 import GUI
from modules.module_1 import Reg_Data
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




if __name__ == '__main__':
    main()