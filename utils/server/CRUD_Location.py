from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utils.server.CRUD_Users import connect_to_mongo
from utils.tools.hash import password_hash
from utils.server.SessionState import save_session
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

def create_location(title, town, desc, tags, image, author, rating, comments):

    if "client" not in st.session_state:
        client = connect_to_mongo()
    else:
        # if the MongoDB connection is already built
        client = st.session_state ['client']

    db = client ['LocatoApp']
    collection = db ['Locations']
