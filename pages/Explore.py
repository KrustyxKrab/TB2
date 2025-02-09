import streamlit as st

from utils.components.LocatoCard import create_card
from utils.components.Sidebar import init_sidebar
from utils.components.HeroSection import hero_section
from utils.components.CreateLocation import create_location

current_page = 'Explore'

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = current_page


if 'current_page' in st.session_state and st.session_state['current_page'] is None:
    st.session_state['current_page'] = 'Explore'

init_sidebar()


if current_page == "Explore":
    hero_section(
        "Let's Explore",
        """🌍 Discover Unique Places Around You!  
    Here, you can explore hidden gems, cozy cafes, and exciting spots recommended by others.  
    Find your next favorite place, save locations you love, and contribute by adding your own discoveries.  
    ✨ **Start exploring now and uncover the best spots near you!**""",
        "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        buttonOne = [{"label": "Create Location", "type": "function", "function": create_location}],
        buttonTwo = [{"label": "Get More Information", 'link': 'pages/Info.py', "type": "switch_page"}],)

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Example Usage
    create_card(title = "Best Coffee Shop",
                description = [{"A cozy place to enjoy your morning coffee."}, {"In the Best Coffee Shop in Lüneburg, you can drink and enjoy tasty coffee and snacks"}],
                id = "coffee_01",
                tags = ["Cafe", "Food & Drink"],
                image = "https://source.unsplash.com/300x200/?coffee",
                additional_info = {"Location": "Berlin", "Rating": "4.5", "Reviews": "200+"},
                buttons = [{"label": "❤"}])

with col2:
    create_card(title = "Best Coffee Shop", description = [{"A cozy place to enjoy your morning coffee."}, {"In the Best Coffee Shop in Lüneburg, you can drink and enjoy tasty coffee and snacks"}],
                id = "coffee_02", tags = ["Cafe", "Food & Drink"],
                image = "https://source.unsplash.com/300x200/?coffee",
                additional_info = {"Location": "Berlin", "Rating": "4.5", "Reviews": "200+"},
                buttons = [{"label": "❤"}])

with col3:
    create_card(title = "Best Coffee Shop", description = [{"A cozy place to enjoy your morning coffee."}, {"In the Best Coffee Shop in Lüneburg, you can drink and enjoy tasty coffee and snacks"}],
                id = "coffee_03", tags = ["Cafe", "Food & Drink"],
                image = "https://source.unsplash.com/300x200/?coffee",
                additional_info = {"Location": "Berlin", "Rating": "4.5", "Reviews": "200+"},
                buttons = [{"label": "❤"}])

with col4:
    create_card(title = "Best Coffee Shop", description = [{"A cozy place to enjoy your morning coffee."}, {"In the Best Coffee Shop in Lüneburg, you can drink and enjoy tasty coffee and snacks"}],
                id = "coffee_04", tags = ["Cafe", "Food & Drink"],
                image = "https://source.unsplash.com/300x200/?coffee",
                additional_info = {"Location": "Berlin", "Rating": "4.5", "Reviews": "200+"},
                buttons = [{"label": "❤"}])


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


# === SEITEN-STEUERUNG ===

# the logic which handles the current page across the multiple pages
# if current_page == login, the login in page is being displayed
# this is a workaround for the button state handler


if st.session_state["current_page"] == "CreateLocation":
    create_location()
    st.rerun()
