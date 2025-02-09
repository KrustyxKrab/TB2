import streamlit as st

def init_sidebar():
    sidebar = st.sidebar

    # ==== ADMIN SECTION ====
    # Admin-Debugging
    #if "user_data" in st.session_state and st.session_state["user_data"] is not None and \
    #        st.session_state['user_data'].get('admin', False):
    #    st.sidebar.header("Debugging")

    #    username = st.session_state["user_data"].get("username")
    #    if username:
    #        user_data = find_user("username", username, update=True)
    #        st.sidebar.write(user_data)
    #    else:
    #        st.sidebar.error("Something went wrong: Username is missing.")
    #else:
    #    st.sidebar.write("No user logged in.")


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