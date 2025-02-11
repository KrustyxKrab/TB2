from utils.server.CRUD_Users import connect_to_mongo
import streamlit as st


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