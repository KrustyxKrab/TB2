import time

import streamlit as st
from utils.server.CRUD_Users import write_user_information
from src.poi_list import poi_tags

def pills(label, b, e):
    with st.container(border = True):
        ### Please select some categories your interested in
        st.markdown(f"{label}")

        #st.pills is quite a new feature
        tag = st.pills("Locato Locations", options = [key for key in range(b, e)],  # Use keys for internal values
                          selection_mode = "multi", format_func = lambda tag: poi_tags[tag]  # Map key - value for display
                          )
        st.markdown(f"You've selected option: {tag}")
        return tag

def setup():

    st.write("Setup your Locato Account")

    tag01 = pills(
        """### Please select categories, you are interested in
        **Select as many categories, as you like**
        1️⃣ Are you interested in: Food & Drink 🍽️🍹
    """, 1, 20)

    tag02 = pills("""2️⃣ Are you interested in: Shopping & Commerce 🛍️🏦? 
    """, 21, 35)

    tag03 = pills("""3️⃣ Are you interested in: Entertainment & Culture 🎭🎶? 
       """, 36, 55)

    tag04 = pills("""4️⃣ Are you interested in: Nature & Outdoor Activities 🌿🏞️? 
           """, 56, 75)

    tag05 = pills("""5️⃣ Are you interested in: Infrastructure & Public Services 🏛️🚉? 
               """, 76, 100)

    # placeholder for the setup form
    placeholder = st.empty()

    with (placeholder.form("Customize")):
        # subheader
        st.subheader("Customize Your Account")

        user_data = st.session_state['user_data']
        username = user_data['username']

        st.write(f"Hello {username}, customize your account settings below:")

        town = st.text_input(label="Main Town", placeholder="Lüneburg")

        col1, col2 = st.columns(2)

        with col1:
            submit_button = st.form_submit_button("Save", type="primary")

        with col2:
            cancel_button = st.form_submit_button("Cancel Changes", type="secondary")
            spinner = st.spinner('Wir passen deinen Account an')

        if submit_button:
            all_tags = [tag for sublist in [tag01, tag02, tag03, tag04, tag05] for tag in sublist]

            if town and all_tags:
                with spinner:
                    try:
                        write_user_information(username, "array", "towns", town)

                        write_user_information(username, "array", "tags", all_tags)

                        st.success(f"Settings updated! Your main town is set to: {town}")

                        time.sleep(5)
                        #usage of st.session_state with current_page as variable and set it to account management -> this leads the user back to the managment page

                        st.session_state["current_page"] = "account_management"

                        # rerun reloads the page and sets it to current_page
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed to update user information: {e}")
            else:
                st.error("Please provide a town name!")
        if cancel_button:
            st.session_state["current_page"] = "account_management"
            # rerun reloads the page and sets it to current_page
            st.rerun()

