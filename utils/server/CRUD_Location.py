import streamlit as st

from utils.server.CRUD_Users import connect_to_mongo
from utils.components.LocatoCard import create_card
from src.poi_list import poi_tags
from utils.tools.card_index import card_index_generator


"""
    What is needed to create a location: 
    
    title - name of the location
    town - where is the location
    
    description - more information about the location 
    
    tags - what is the location (some tags of the poi_tag list)
    
    rating 
    
    comments

"""

def create_location(title, town, desc, tags, image=None, author=None, id=None):
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
             "town": town,
             "desc": desc,
             "tags": tags,
             "id": id,
             "image": image,
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

        if filter is "author":
            # gets user_data tags
            if st.session_state['user_data']:
                username = st.session_state['user_data']['username']
                query = {"author": username}

        elif filter is "user":
            # gets user_data tags
            if st.session_state ['user_data']:
                user_tags = st.session_state ['user_data'] ['tags']

                # if user_tags is only one number and not a list
                if isinstance(user_tags, int):
                    user_tags = [user_tags]

            else:
                user_tags = []

            # if only a few tags are stored for the user
            if len(user_tags) < 3:
                query = {}  # Show all locations if no user tags exist
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

        else:
            query = {}  # Show all locations if no user tags exist

        if query is not None:
            # fetches the data from mongo
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
            with columns [col_index]:

                create_card(
                    title=location.get("title", "Unknown Title"),
                    description=location.get("desc", ["No description available"]),
                    id=location.get("id", "Unknown ID"),
                    tags=[poi_tags.get(tag, f"Tag {tag}") for tag in tags],
                    image=location.get("image", None),
                    additional_info={"Town": location.get("town", "Unknown Town"), "Author": location.get("author", "Unknown Author")}
                )

    except Exception as e:
        st.error(f"⚠️ Error fetching locations: {e}")
        print(f"❌ Could not fetch locations - Error: {e}")

