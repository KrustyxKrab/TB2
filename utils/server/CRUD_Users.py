import streamlit as st

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utils.tools.hash import password_hash
from utils.server.SessionState import save_session
#from utils.server.alert_admin import alert_admin
import time

# ==== GENERAL CONNECTION FUNCTION ====


def connect_to_mongo(retries=5, delay=2):
    """
    Connect to MongoDB with automatic retries and a fallback mechanism.
    """
    # Import credentials from Streamlit secrets
    user = st.secrets ['username']
    db_password = st.secrets ['password']

    # MongoDB connection URI
    uri = f"mongodb+srv://{user}:{db_password}@locato.8njtn.mongodb.net/?retryWrites=true&w=majority&appName=Locato"

    # Attempt to connect with retries
    for attempt in range(retries):
        try:
            client = MongoClient(uri, server_api = ServerApi('1'))
            client.admin.command('ping')  # Check if MongoDB is alive

            # Save connection to session state
            save_session("client", client)

            return client
        except Exception as e:
            st.warning(f"⏳ Retry {attempt + 1}/{retries}: MongoDB not responding... {e}")
            time.sleep(delay * (2 ** attempt))  # Exponential backoff

    st.error("MongoDB is down. Switching to fallback solution...")

    #alert_admin()

    return fallback_solution()


def fallback_solution():
    """
    Fallback mechanism:
    1. Try reading from a read-only secondary MongoDB node.
    """
    try:
        # Attempt to connect to a secondary node (read-only)
        secondary_uri = f"mongodb+srv://{st.secrets ['backup_user']}:{st.secrets ['backup_password']}@locato.8njtn.mongodb.net/?retryWrites=true&w=majority&appName=Locato"
        secondary_client = MongoClient(secondary_uri, server_api = ServerApi('1'))
        secondary_client.admin.command('ping')  # Test connection
        st.warning("⚠️ Connected to a read-only MongoDB replica.")
        return secondary_client
    except Exception as e:
        st.error("⚠️ Fallback Connection to MongoDB also unavailable. Contacted locato admin")


# ==== CREATE USER ====
def create_user(name, username, email, password, id):  #create
    try:
        # If the MongoDB Connection is not built previously
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            # if the MongoDB connection is already built
            client = st.session_state['client']

        db = client['LocatoApp']
        collection = db['users']

        hashed_password = password_hash(password)

        user_document = {
            "name": name,
            "username": username,
            "email": email,
            "password": hashed_password,
            "id": id,
            "admin": False,
            "likes": [],
            "towns": [],
            "tags": [],
        }

        if collection.insert_one(user_document):
            # stores the document in the session state
            st.session_state["user_data"] = user_document
            user_data = st.session_state["user_data"]
            st.write(f"User Data = {user_data} (ERRORCODE create_user)")
            print(f"Data inserted with the username {username}")

        else:
            st.error("User has not been created!")

    except Exception as e:
        print(f"Could not connect to MongoDB - Error: {e}")


# ==== FIND USER AND UPDATE STATE ====
def find_user(key, value, update=False):
    """
    Fetch user data from the database.
    If `update=True`, it forces a new database fetch.
    Otherwise, it returns the session state value if available.
    """

    if not update and "user_data" in st.session_state and st.session_state["user_data"]:
        return st.session_state["user_data"]  # Use cached session data if update is False

    try:
        # Ensure MongoDB connection
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["users"]

        # Fetch user from database
        user = collection.find_one({key: value})

        # Update session state with fresh data
        if user:
            st.session_state["user_data"] = user
            print(f"User found in DB with {key}: {value}")
            return user
        else:
            print(f"No user found with {key}: {value}")
            return None

    except Exception as e:
        print(f"Error fetching user from DB: {e}")
        return None

# ==== WRITE INFORMATION TO USER ====
def write_user_information(username, type, key, value):  # write/ update
    try:
        # Verbindung zu MongoDB herstellen
        client = st.session_state['client']
        user_data = st.session_state['user_data']

        # database
        db = client['LocatoApp']
        collection = db['users']

        # Log the username and key-value being updated
        print(f"Updating user: {username}, key: {key}, value: {value}")

        # searches the user with the username
        if not user_data:
            # security (if no user is found - should not be possible)
            print(f"No user found in session state for username: {username}")
            return

        # value is added to key
        if type == "array":
            result = collection.update_one(
                {"username": username},  # Filter
                {"$addToSet": {key: value}}
            )
        elif type == "string":
            result = collection.update_one(
                {"username": username},  # Filter
                {"$set": {key: value}}
            )
        else:
            print("Error - please enter a valid type")
            return

        # Log the result of the database update
        print(f"Update result: {result.modified_count} document(s) modified.")

    except Exception as e:
        print(f"Error occurred while writing information: {e}")

# ==== UPDATE USER INFORMATION ====
def update_user_field(username, key, value, update_type):
    try:
        # Ensure MongoDB connection
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["users"]

        # Log the update operation
        print(f"Updating user: {username}, key: {key}, value: {value}, update_type: {update_type}")

        # Define update operation based on update_type
        if update_type == "set":
            update_operation = {"$set": {key: value}}  # Directly update a field
        elif update_type == "addToSet":
            update_operation = {"$addToSet": {key: value}}  # Add value to array

        #elif update_type == "push":
        #    update_operation = {"$push": {key: value}}  # Append value to array (even if duplicate)
        else:
            print("Error - Invalid update type! Use 'set', 'addToSet', or 'push'.")
            return

        # Perform the update operation
        result = collection.update_one({"username": username}, update_operation)

        # Log the result
        if result.modified_count > 0:
            print(f"Successfully updated user {username}: {key} -> {value}")
        else:
            print(f"No changes made for user {username} (field may already have the value)")

    except Exception as e:
        print(f"Error updating user information: {e}")