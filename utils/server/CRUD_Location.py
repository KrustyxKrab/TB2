import streamlit as st

from utils.server.CRUD_Users import connect_to_mongo
from utils.components.LocatoCard import create_card
from src.poi_list import poi_tags
from utils.tools.card_index import card_index_generator


"""
    What is needed to create a location: 
    
    title - name of the location
    address - where is the location
    
    description - more information about the location 
    
    tags - what is the location (some tags of the poi_tag list)
    
    rating 
    
    comments

"""

def create_location(title, desc, tags, image=None, address=None, author=None, id=None):
    try:
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            # if the MongoDB connection is already built
            client = st.session_state['client']

        db = client['LocatoApp']
        collection = db['locations']

        location_document = \
            {"title": title,
             "desc": desc,
             "tags": tags,
             "id": id,
             "image": image,
             "address": address,
             "author": author,
             "rating": 0,
             "comments": None,
             }

        if collection.insert_one(location_document):
            # stores the document in the session state
            st.write(f"Location Data = {location_document}")
            print(f"Location inserted by {author}")


        else:
            st.error("Location has not been created!")

    except Exception as e:
        print(f"Could not connect to MongoDB - Error: {e}")


def find_location(key, value):
    try:

        client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["location"]

        # Fetch user from database
        location = collection.find_one({key: value})

        # Update session state with fresh data
        if location:
            print(f"Location found in DB with {key}: {value}")
            return location
        else:
            print(f"No location found with {key}: {value}")
            return None

    except Exception as e:
        print(f"Error fetching user from DB: {e}")
        return None

def read_location(filter):
    try:
        # connects to database
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["locations"]

        print("initialized read")

        if filter == "author":
            # gets user_data tags
            if "user_data" in st.session_state and st.session_state['user_data'] is not None:
                username = st.session_state['user_data']['username']
                query = {"author": username}

                print("filter author")

        elif filter == "user":
            # gets user_data tags
            if "user_data" in st.session_state and st.session_state['user_data'] is not None:
                user_tags = st.session_state['user_data']['tags']

                print("filter user part one")

                # if user_tags is only one number and not a list
                if isinstance(user_tags, int):
                    user_tags = [user_tags]

            else:
                user_tags = []
                print("if no user information are stored")

            # if only a few tags are stored for the user
            if len(user_tags) < 3:
                query = {}  # Show all locations if no user tags exist
                st.write("Please configure you account for best fitting results.")
            else:
                query = {"tags": {"$in": user_tags}}

        elif filter == "id":
            likes = []  # Default empty list
            # Check if user_data exists and has 'Likes'
            if 'user_data' in st.session_state and st.session_state['user_data']:
                user_data = st.session_state['user_data']
                if 'Likes' in user_data:
                    likes = user_data['Likes']

                    # Ensure likes is a list
                    if isinstance(likes, int):
                        likes = [likes]
            # Only set query if likes is not empty
            if likes:
                query = {"id": {"$in": likes}}
            else:
                query = None
                return

        elif filter == "all":
            print("filter all")
            query = {}  # Show all locations if no user tags exist

        else:
            st.error("Something went wrong... please reload")

        if query is not None:
            print("query not None")
            # fetches the data from mongo
            locations = list(collection.find(query))

        else:
            return

        columns = st.columns(4)
        card_index = card_index_generator()

        # use of create_Card to display location
        for location in locations:
            tags = location.get("tags", [])

            # if tags is only one integer, convert tags to list
            if isinstance(tags, int):
                tags = [tags]

            col_index = next(card_index)
            with columns [col_index]:

                print("Create Card")
                create_card(
                    title=location.get("title", "Unknown Title"),
                    description=location.get("desc", ["No description available"]),
                    id=location.get("id", "Unknown ID"),
                    tags=[poi_tags.get(tag, f"Tag {tag}") for tag in tags],
                    image=location.get("image", None),
                    address=location.get("address", "No Address given"),
                    additional_info={"Author": location.get("author", "Unknown Author")}
                )
                print("after creation")

    except Exception as e:
        st.error(f"⚠️ Error fetching locations: {e}")
        print(f"❌ Could not fetch locations - Error: {e}")

def admin_rights():
    try:
        # connects to database
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["locations"]

        query = {}

        locations = list(collection.find(query))

        columns = st.columns(4)
        card_index = card_index_generator()

        # use of create_Card to display location
        for location in locations:
            tags = location.get("tags", [])

            # if tags is only one integer, convert tags to list
            if isinstance(tags, int):
                tags = [tags]

            col_index = next(card_index)
            with columns[col_index]:

                create_card(title = location.get("title", "Unknown Title"),
                    description = location.get("desc", ["No description available"]), id = location.get("id", "Unknown ID"),
                    tags = [poi_tags.get(tag, f"Tag {tag}") for tag in tags], image = location.get("image", None),
                    additional_info = {"Author": location.get("author", "Unknown Author")},
                    buttonLabel = "➖",
                    buttonText = "Delete"),

    except Exception as e:
        st.error(f"⚠️ Error with admin operation: {e}")
        print(f"❌ Error with admin operation - Error: {e}")


def deleteLocation(key, value):
    "key should be id"

    try:
        # connects to database
        if "client" not in st.session_state:
            client = connect_to_mongo()
        else:
            client = st.session_state["client"]

        db = client["LocatoApp"]
        collection = db["locations"]

        collection.delete_one({f"{key}": f"{value}"})

    except Exception as e:
        st.error(f"⚠️ Error deleting location: {e}")
        print(f"❌ Could not delete location - Error: {e}")