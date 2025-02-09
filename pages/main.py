import streamlit as st

from utils.components.HeroSection import hero_section

query_params = st.query_params
current_page = query_params.get("page", "main")

if current_page == "main":
    if st.session_state['logged_in'] is False:
        hero_section(
            "Welcome to Locato",
            "A social app for real life - contribute to a society of social hotspots all around the world",
            "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            buttonOne=[{"label": "Register Now", 'link': 'pages/Register.py', "type": "switch_page"}],
            buttonTwo=[{"label": "Log-In", 'link': 'pages/Login.py', "type": "switch_page"}]
        )

    elif st.session_state ['logged_in'] is True:
        hero_section("Locato",
            "Your social app for real life - contribute to a society of social hotspots all around the world",
            "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            buttonOne = [{"label": "Explore Now", 'link': 'pages/Explore.py', "type": "switch_page"}],
            buttonTwo = [{"label": "Create Now", 'link': 'pages/CreateLocation.py', "type": "switch_page"}])

    else:
        st.error('Sorry - We have a Problem - Please try to reload or contact support')

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