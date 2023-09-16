import streamlit as st
from streamlit_option_menu import option_menu

###############################################################
# +=========================================================+ #
# | Menu Bar - 1] Sidebar  2] Horizontar  3] Custom         | #
# +=========================================================+ #
###############################################################
EXAMPLE_NO = st.selectbox(
    'Choose the menu?',
    ('Sidebar', 'Horizontal', 'Custom'))


def streamlit_menu(example=1):
    ###############################################################
    # +=========================================================+ #
    # | Menu Bar - 1] Sidebar                                   | #
    # +=========================================================+ #
    ###############################################################
    if example == "Sidebar":
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    ###############################################################
    # +=========================================================+ #
    # | Menu Bar - 2] Horizontar                                | #
    # +=========================================================+ #
    ###############################################################
    if example == "Horizontal":
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    ###############################################################
    # +=========================================================+ #
    # | Menu Bar - 3] Custom                                    | #
    # +=========================================================+ #
    ###############################################################
    if example == "Custom":
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "blue"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
