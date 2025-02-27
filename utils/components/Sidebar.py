import streamlit as st

# init the sidebar, calls the sidebar (a bit superfluous at the moment but could be used in the future...)

def init_sidebar():
    sidebar = st.sidebar

    st.markdown("""
        <style>
            section[data-testid="stSidebar"] {
                width: 100px !important;
            }
            [data-testid="collapsedControl"] {
                display: None;
            }
        </style>
    """, unsafe_allow_html=True)