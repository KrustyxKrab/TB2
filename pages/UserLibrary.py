import streamlit as st

from utils.server.CRUD_Users import update_user_field
from utils.components.AccountSetup import setup

st.title('Your Locato Locations')

st.write(f"Welcome, {st.session_state['user_data']['username']}!")

if st.session_state['user_data']['admin'] is True:
    st.write('You are an admin of Locato - Congratulations')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Fetch Information"):
        for item in st.session_state.items():
            st.write(item)

with col2:
    if st.button("Customize Account"):
        # current page which is setup
        st.session_state ["current_page"] = "setup"

        # loads current page
        st.rerun()

with col3:
    if st.button("Clear Tags"):
        username = st.session_state['user_data']['username']
        update_user_field(username, "tags", [], "set")
        st.session_state["current_page"] = "account_management"
        st.rerun()

if st.button("Log Out", type="primary"):
    st.session_state['user_data'] = None
    st.session_state['logged_in'] = False
    st.session_state["current_page"] = "login"
    st.rerun()




#==================

elif st.session_state["current_page"] == "setup":
    setup()

