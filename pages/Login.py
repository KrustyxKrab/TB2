import streamlit as st

from utils.server.CRUD_Users import find_user
from utils.components.Sidebar import init_sidebar
from utils.tools.hash import verify_password


init_sidebar()

# TITLE
st.title('Locato Account')

# === Session State Initialisieren ===
if "logged_in" not in st.session_state or st.session_state['logged_in'] is None:
    st.session_state["logged_in"] = False

if "AccountCustomized" not in st.session_state:
    st.session_state["AccountCustomized"] = False

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "login"  # by default current_page = login (main login page)

if "user_data" not in st.session_state:
    st.session_state["user_data"] = None  # Ensure user_data is a dictionary


if "user_data" in st.session_state and st.session_state["user_data"] is not None and st.session_state['user_data']['admin'] is True:
    st.sidebar.header("Debugging")

    # Ensure user_data exists before accessing it
    if "user_data" in st.session_state and st.session_state["user_data"] is not None:
        username = st.session_state["user_data"].get("username")  # Use .get() to prevent KeyErrors

        if username:
            user_data = find_user("username", username, update=True)  # Force database update
            st.sidebar.write(user_data)  # Show the fresh database data
        else:
            st.sidebar.error("Something went wrong: Username is missing.")
    else:
        st.sidebar.write("No user logged in.")


# === LOGIN SEITE ===
def login():
    if st.session_state["logged_in"] is True:
        return None  # if the user is already logged in, just leave

    placeholder = st.empty()

    with placeholder.form("login_form"):
        st.subheader("Log-In Now")
        username = st.text_input("Enter username", placeholder="username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Log In")

        if submit_button:
            with st.spinner('Wir prüfen deinen Account'):
                try:
                    user_data = find_user("username", username)

                    if user_data and verify_password(password, user_data["password"]):
                        st.success("Login successful!")

                        #usage of session_state -> safe the user progress for optimal UX

                        st.session_state["user_data"] = user_data
                        st.session_state["logged_in"] = True

                        # sets the current_page to "account_management" which is the logged in area
                        st.session_state["current_page"] = "account_management"

                        # rerun reloads the page -> sets it to "account management"
                        st.rerun()  # Seite neu laden
                    else:
                        st.error("Invalid credentials!")

                except Exception as e:
                    st.error(f"An error occurred: {e}")

    return None

# === SEITEN-STEUERUNG ===

# the logic which handles the current page across the multiple pages
# if current_page == login, the login in page is being displayed
# this is a workaround for the button state handler

if st.session_state["current_page"] == "login":
    login()

