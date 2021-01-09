import streamlit as st
from modules.module_0 import Module_0
from modules.module_1 import Module_1
# section_zero, pars_arg, , \
#     section_one, section_two, section_three, section_four, \
#     section_five

def main():
    #tb._SYMBOLIC_SCOPE.value = True

    intro_butt = st.sidebar.checkbox('1) Introduction', key=None)

    gui = Module_0()

    if intro_butt:
        gui.intro()

    data_but = st.sidebar.checkbox('2) Data Entry', key=None)

    if data_but:

        data = Module_1()



if __name__ == '__main__':
    main()