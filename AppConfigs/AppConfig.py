import streamlit as st

"""

During my work on the App Locato I tried to find a lot of workaround for many problems. One interesting finding is: 
When I use the st.switch_page(link) function for example in the hero_section file, the buttons only work, when I have
introduced the app where I want to go inside this file (for example the information file)... I couldn't manage to make it work,
without listing the file here before referring to it. 

To make it work, all the pages, which I want to refer to, need to be visible in the st.navigation()

"""


pages = {
    "Navigation": [
        st.Page('pages/main.py', title="Home", default = True, icon="🏡"),
        st.Page("pages/Explore.py", title="Explore", icon="🧭"),
        st.Page("pages/Info.py", title="Information", icon="ℹ️"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],

    "Your Account": [
        st.Page("pages/Login.py", title="Log-In", icon="👥"),
        st.Page("pages/Register.py", title="Create Account", icon="➕"),
    ],
}



after_login_pages = {
    "Navigation": [
        st.Page('pages/main.py', title="Home", default = True, icon="🏡"),
        st.Page("pages/Explore.py", title="Explore", icon="🧭"),
        st.Page("pages/CreateLocation.py", title="Create Location", icon="📍"),
        st.Page("pages/Info.py", title="Information", icon="ℹ️"),
    ],

    "Your Account": [
        st.Page("pages/UserLibrary.py", title="Your Account", icon="👤"),
    ],
}
