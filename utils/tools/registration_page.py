import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import bcrypt

def intro_page():
    st.title("Welcome")

    log_in_button = st.button("Log-In")

    if log_in_button:
        login()

    register_button = st.button("Register Now")

    if register_button:
        register()

@st.cache_resource
def connect_to_mongo():
    # import the name & password from .streamlit secrets
    user = st.secrets['username']
    db_password = st.secrets['password']

    uri = f"mongodb+srv://{user}:{db_password}@mvpcluster.jb3xz.mongodb.net/?retryWrites=true&w=majority&appName=MVPCluster"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

def insert_data():
    try:
        client = connect_to_mongo()
        print("Connected successfully!")
    except:
        print("Could not connect to MongoDB")

    # database
    db_name = 'Streamlit'
    collection_name = "Streamlit_users"

    db = client[db_name]
    collection = db[collection_name]


    user_document = {
        "name": name,
        "username": user_name,
        "email": email,
        "password": hash,
        "age": age,
    }

    user = collection.insert_one(user_document)
    print(f"Data inserted with the username {user_name}")

def login():
    st.title("Log-In")

    # Create placeholders
    form_placeholder = st.empty()
    message_placeholder = st.empty()

    with form_placeholder.form("log_in_form"):
        # Input form title
        st.subheader("Log-In")
        # Input fields for user
        user_name = st.text_input("Enter username", placeholder="username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Send")

    # Move the submit button logic outside the 'with' block
    if submit_button:
        # Debug: Print the values of user inputs
        print(f"Debug: user_name = {user_name}")
        print(f"Debug: password = {password}")

        print("Debug: Submit button clicked")
        try:
            client = connect_to_mongo()
            print("Debug: Connected to MongoDB client successfully!")
        except Exception as e:
            print(f"Debug: Could not connect to MongoDB. Exception: {e}")
            st.error("Database connection failed.")
            st.stop()

        # Database
        db_name = 'Streamlit'
        collection_name = "Streamlit_users"

        db = client[db_name]
        collection = db[collection_name]
        print(f"Debug: Accessed collection '{collection_name}' in database '{db_name}'")

        # Check if the user exists
        user_document = collection.find_one({"username": user_name})
        print(f"Debug: user_document = {user_document}")

        if user_document:
            print("Debug: User found in database")
            # User exists, now check password
            stored_password_hash = user_document['password']  # Assuming password is stored as a hash
            print(f"Debug: stored_password_hash = {stored_password_hash}")

            # If stored_password_hash is a string, encode it; otherwise, use it directly
            if isinstance(stored_password_hash, str):
                stored_hash_bytes = stored_password_hash.encode('utf-8')
                print("Debug: stored_password_hash encoded to bytes")
            else:
                stored_hash_bytes = stored_password_hash  # Already bytes
                print("Debug: stored_password_hash is already bytes")

            # Encode the entered password
            password_bytes = password.encode('utf-8')
            print(f"Debug: password_bytes = {password_bytes}")

            # Verify the password
            if bcrypt.checkpw(password_bytes, stored_hash_bytes):
                print("Debug: Password verification successful")
                st.success("Logged in successfully!")

                # Clear the form
                form_placeholder.empty()

                clearname = user_document['name']
                age = user_document['age']
                email = user_document['email']

                print(f"Debug: User data - Name: {clearname}, Age: {age}, Email: {email}")

                markdown_message = f"""
                ### Welcome back, {user_name}!
                Your data is stored securely:

                - **Name:** {clearname}
                - **Age:** {age}
                - **Email:** {email}
                """

                # Display the message
                message_placeholder.markdown(markdown_message)

            else:
                print("Debug: Password verification failed")
                st.error("Incorrect password")
        else:
            print("Debug: Username not found in database")
            st.error("Username not found")



def register():
    global user_name, email, password, age, name
    st.title("Registration")

    # register form holder
    placeholder = st.empty()

    with placeholder.form("registration_form"):
        # input form title
        st.subheader("Register Now")
        # input fields for user
        name = st.text_input("Enter your name", placeholder="Max Mustermann")
        user_name = st.text_input("Enter username", placeholder="username")
        email = st.text_input("Enter email address", placeholder="max.mustermann@mail.de")
        password = st.text_input("Password", type="password")
        repeat_password = st.text_input("Repeat Password", type="password")
        age = st.number_input("Enter your age", min_value=18, step=1,)
        #Ask for more information
        submit_button = st.form_submit_button("Send")


        if submit_button:
            # TODO: Store the data before clearing
            # check inputs
            if len(user_name) < 1 and len(password) < 1:
                st.error("Type in username & password")
            elif len(user_name) < 1:
                st.error("Type in username")
            elif len(password) < 1:
                st.error("Type in password")
            elif password != repeat_password:
                st.error("The passwords do not match")

            else:
                # clear the placeholder form
                bytes = password.encode('utf-8')
                salt = bcrypt.gensalt()
                hash = bcrypt.hashpw(bytes, salt)
                print(hash)

                insert_data()

            placeholder.empty()

intro_page()
