import streamlit as st
def save_session(key, value):
    if key not in st.session_state:
        st.session_state[key] = value
    return st.session_state[key]