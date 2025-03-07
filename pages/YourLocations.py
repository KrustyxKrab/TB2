import streamlit as st
from utils.server.CRUD_Location import read_location

st.title("Your Locations")
st.write("These are the Locations, you have created.")

# read with different filter. here: author for own locations
read_location("author")

st.title("Your Liked Locations")

# read with different filter. here: id for liked locations
read_location("id")
if read_location("id") == None:
    st.write("You have not Liked any Location yet")

st.markdown("""
    <style>
        /* Forces Streamlit content to use full width */
        [data-testid="stAppViewContainer"] {
            max-width: 100vw;
            padding: 0;
        }

        /* Expands the main content container */
        [data-testid="stMainBlockContainer"] {
            max-width: 100% !important;
            padding-top: 5rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        /* Removes margins from main content */
        [data-testid="stMain"] {
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)