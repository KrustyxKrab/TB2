import streamlit as st

from utils.server.CRUD_Users import create_user, find_user
from utils.tools.generate_id import generate_unique_id
from utils.components.AccountSetup import setup
from utils.components.Sidebar import init_sidebar

init_sidebar()

st.title("Registration")

# Found work around with st.session_state
if "registered" not in st.session_state:
    st.session_state["registered"] = False

if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

def register():

    # Ensure the session state key exists
    if "registered" not in st.session_state:
        st.session_state["registered"] = False

    # If already logged in, clear the form and return
    if st.session_state["registered"]:
        return None

    # Register form holder
    placeholder = st.empty()
    username = None

    # Create a registration form inside the placeholder
    with placeholder.form("registration_form"):
        st.subheader("Register Now")
        name = st.text_input("Enter your name", placeholder="Max Mustermann")
        username = st.text_input("Enter username", placeholder="username")
        email = st.text_input("Enter email address", placeholder="max.mustermann@mail.de")
        password = st.text_input("Password", type="password")
        repeat_password = st.text_input("Repeat Password", type="password")
        st.markdown("""<p>Your password is securely hashed and cannot be read from anybody else!<br>
        *By pressing 'Send', you allow Locato to safe and process your data!</p>""", unsafe_allow_html=True)
        submit_button = st.form_submit_button("Send")

        # Process the form submission
        if submit_button:
            if len(username) < 1 and len(password) < 1:
                st.error("Type in username & password")
            elif len(username) < 1:
                st.error("Type in username")
            elif len(password) < 1:
                st.error("Type in password")
            elif password != repeat_password:
                st.error("The passwords do not match")
            elif find_user("username", username):
                st.error(f"This username is already used - Do you want to Log In?")
                st.page_link("pages/Login.py", label="Click here to Log In")
            else:
                unique_id = generate_unique_id(type = "user")
                create_user(name, username, email, password, unique_id)
                st.session_state["registered"] = True
                st.session_state["logged_in"] = True
                st.rerun()
                return username

    return None


def load_customization():
    print("load custom")

    if "user_data" in st.session_state and st.session_state["user_data"] is not None:
        #st.write(f"user_data = {st.session_state['user_data']} (SUCCESS)")
        setup()
    else:
        print("else triggered in load customization")
        st.write(f"user_data = {st.session_state.get('user_data', 'None')} (ERRORCODE register)")


# main function
username = register()

if st.session_state.get("registered", True):
    load_customization()