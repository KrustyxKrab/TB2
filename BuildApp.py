import streamlit as st
from utils.components.Sidebar import init_sidebar
from AppConfigs.AppConfig import pages, after_login_pages, after_login_pages_ADMIN

#st.set_page_config(page_title="Locato App", initial_sidebar_state="collapsed", layout="wide")

st.set_page_config(
    page_title="Locato",
    page_icon="🧭"
)


with st.spinner("Getting the App ready"):
    init_sidebar()

    nav = st.navigation(pages)


    if "user_data" not in st.session_state:
        st.session_state['user_data'] = None

    if "logged_in" not in st.session_state:
        st.session_state['logged_in'] = False

    if "user_data" in st.session_state and st.session_state["user_data"] is not None:
        if st.session_state["user_data"]['username'] and st.session_state["user_data"]["admin"] is False:
            nav = st.navigation(after_login_pages)

        if st.session_state["user_data"]['username'] and st.session_state["user_data"]["admin"] is True:
            nav = st.navigation(after_login_pages_ADMIN)

            if "redirected" not in st.session_state:
                st.session_state["redirected"] = True  # Prevent multiple redirects
                st.switch_page("pages/UserLibrary.py")

nav.run()

