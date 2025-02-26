import streamlit as st

from utils.server.CRUD_Users import update_user_field
from utils.server.CRUD_Users import find_user
from utils.components.AccountSetup import setup
from utils.server.SessionState import save_session

st.title('Your Locato Locations')

st.write(f"Welcome, {st.session_state ['user_data'] ['username']}!")

if st.session_state ['user_data'] ['admin'] is True:
    st.write('You are an admin of Locato - Congratulations')

# ========== CHANGE DATA SECTION =========

#container
data_container = st.container(border = True)

# edit mode is a st.session_state variable
if "edit_mode" not in st.session_state:
    st.session_state["edit_mode"] = False

name = st.session_state["user_data"]["name"]
username = st.session_state["user_data"]["username"]
email = st.session_state["user_data"]["email"]

if not st.session_state["edit_mode"]:
    with data_container:

        # displays the data of the user
        user_data_wpassword = find_user("username", username, update = True)
        password = user_data_wpassword ["password"]

        # disabled (without the edit mode)
        st.text_input(label = "Name", placeholder = name, disabled = True)
        st.text_input(label = "Username", placeholder = username, disabled = True)
        st.text_input(label = "Email", placeholder = email, disabled = True)
        st.text_input(label = "Password", placeholder = "••••••••••", disabled = True)

        change_data = st.button(label = "Change Data")

        # rerun when the button is pressed
        if change_data:
            st.session_state["edit_mode"] = True
            st.rerun()

# change data with edit_mode
else:
    with data_container:
        new_name = st.text_input(label = "New Name", placeholder = name)
        new_username = st.text_input(label = "New Username", placeholder = username)
        new_email = st.text_input(label = "New Email", placeholder = email)

        st.button(label = "Change Password", disabled = True)

        colA, colB = st.columns(2)
        with colA:
            save = st.button(label = "Save Changes", type = "primary", use_container_width = True)

        with colB:
            cancel = st.button(label = "Cancel", type = "secondary", use_container_width = True)

        # when the button is pressed, validate the input and send it to mongo
        if save:
            if len(new_name) < 1:
                st.error("Type in a name")
            elif len(new_username) < 1:
                st.error("Type in a username")
            elif find_user("username", new_username):
                st.error(f"This username is already used - Take a different username!")
            else:
                update_user_field(username, "name", new_name, "set")
                update_user_field(username, "username", new_username, "set")
                update_user_field(username, "email", new_email, "set")

                st.session_state["user_data"]["name"] = new_name
                st.session_state["user_data"]["username"] = new_username
                st.session_state["user_data"]["email"] = new_email

                st.session_state["edit_mode"] = False
                # switches back to non edit_mode with edit mode = False
                st.rerun()

col1, col2 = st.columns(2)

if st.button("Customize Account"):
    # current page which is setup
    st.session_state["current_page"] = "setup"
    # loads current page
    st.rerun()

st.write("Re-Customize your Account and change your preferred Locations")

if st.button("Clear Tags"):
    username = st.session_state ['user_data'] ['username']
    update_user_field(username, "tags", [], "set")
    st.session_state ["current_page"] = "account_management"
    st.rerun()
st.write("For sake of transparency, you can reset your tags, which are used to recommend you locations.")

if st.session_state['user_data']['admin'] is True:
    if st.button("Fetch Information"):
        for item in st.session_state.items():
            st.write(item)

if st.button("Log Out", type = "primary", use_container_width = True):
    st.session_state['user_data'] = None
    st.session_state['logged_in'] = False
    st.session_state["current_page"] = "login"
    st.rerun()

# offers logout and the re-log in due to the current_page variable

# =========

elif st.session_state["current_page"] == "setup":
    setup()
