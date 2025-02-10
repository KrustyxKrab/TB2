import streamlit as st

from utils.components.HeroSection import hero_section

query_params = st.query_params
current_page = query_params.get("page", "main")

if current_page == "main":
    if st.session_state['logged_in'] is False:
        st.session_state['current_page'] = "login"
        hero_section(
            "Welcome to Locato",
            """Connect. Discover. Contribute.  
            
            In a world dominated by digital interactions, **Locato** brings people back to real-life experiences. Our platform is designed to help you discover the best places around you, connect with like-minded individuals, and contribute to a thriving community of social hotspots.""",
            "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            buttonOne=[{"label": "Register Now", 'link': 'pages/Register.py', "use": "switch_page", "type": "primary"}],
            buttonTwo=[{"label": "Log-In", 'link': 'pages/Login.py', "use": "switch_page"}]
        )
        with st.container(border = True):
            st.markdown("""
            ### What is Locato?
            Locato is more than just a location-based app – it’s a **movement** that encourages real-world connections. Whether you’re looking for a cozy café, a vibrant co-working space, or a hidden gem in your city, Locato helps you find and share the best spots.

            ### Why Join Locato?
            ✅ **Discover Unique Places** – Find the best local hotspots curated by the community.  
            ✅ **Share Your Favorites** – Recommend places that inspire and energize you.  
            ✅ **Meet Like-Minded People** – Connect with others who share your interests.  
            ✅ **Contribute to Your Community** – Help create a more vibrant and connected social landscape.  

            ### Your World, Your Experience
            Whether you're an explorer, a food lover, a digital nomad, or just someone looking to make new connections, **Locato gives you the tools to shape your social world**.

            Join us today and be part of a growing community that values real-life experiences. **Let’s make the world more connected, one hotspot at a time!** 🚀""")


    elif st.session_state['logged_in'] is True:
        hero_section("Locato",
            "Your social app for real life - contribute to a society of social hotspots all around the world",
            image = "https://images.unsplash.com/photo-1716146410134-5e152c41827a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            #imageseq = ["https://images.unsplash.com/photo-1663516003203-63867620cfda?q=80&w=2664&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "https://images.unsplash.com/photo-1586802263591-61e3ccc051e0?q=80&w=2716&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "https://images.unsplash.com/photo-1586804297194-37377f8e4875?q=80&w=2752&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"],
            buttonOne = [{"label": "Explore Now", 'link': 'pages/Explore.py', "use": "switch_page", "type": "primary"}],
            buttonTwo = [{"label": "Create Now", 'link': 'pages/CreateLocation.py', "use": "switch_page"}])

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