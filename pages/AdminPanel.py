import streamlit as st

from utils.server.CRUD_Location import admin_rights

st.title("Admin Dahsboard")
st.write("Review Users, Locations and edit them")

admin_rights()