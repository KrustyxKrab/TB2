import streamlit as st

from utils.components.Sidebar import init_sidebar
from utils.components.HeroSection import hero_section
from utils.server.CRUD_Location import read_location

# variable current_page set to explore (default for this page)
current_page = 'Explore'

# st.session_state
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = current_page

if 'current_page' in st.session_state and st.session_state['current_page'] is None:
    st.session_state['current_page'] = 'Explore'

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

init_sidebar()

# when user is logged in
if current_page == "Explore" and st.session_state["logged_in"] is True:
    hero_section(
        "Let's Explore",
        """🌍 Discover Unique Places Around You!  
    Here, you can explore hidden gems, cozy cafes, and exciting spots recommended by others.  
    Find your next favorite place, save locations you love, and contribute by adding your own discoveries.  
    ✨ **Start exploring now and uncover the best spots near you!**""",
        "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        buttonOne = [{"label": "Create Location", "use": "switch_page", "link": "pages/CreateLocation.py", "type": "primary"}],
        buttonTwo = [{"label": "Get More Information", 'link': 'pages/Info.py', "use": "switch_page"}],)

# when user is not logged in
elif st.session_state['logged_in'] is False:
    hero_section("Let's Explore", """🌍 Discover Unique Places Around You!  
    Here, you can explore hidden gems, cozy cafes, and exciting spots recommended by others.  
    Find your next favorite place, save locations you love, and contribute by adding your own discoveries.  
    ✨ **Start exploring now and uncover the best spots near you!**""",
        "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        buttonOne = [{"label": "Log-In to Create Location", "use": "switch_page", "link": "pages/Login.py", "type": "primary"}],)

# should not occur but error handling
else:
    print("Error")
    st.sidebar.write(st.error("Something went wrong! Please reload or try again!"))

# Locations when logged in
if "user_data" in st.session_state and st.session_state["user_data"] is not None:
    st.title("Locations for You")
    read_location("user")

# all locations
st.title("All Locations")
read_location("all")


st.markdown("""
<style>
/* Style columns */
[data-testid="column"] {
    box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    border-radius: 15px;
    padding: 0;
} 

</style>""",
            unsafe_allow_html=True)

# css for wide layout
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
            padding-top: 1rem;
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

# switch page when button pressed
if st.session_state["current_page"] == "CreateLocation":
    st.switch_page("pages/CreateLocation.py")
    st.rerun()
