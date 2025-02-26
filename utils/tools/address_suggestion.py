import streamlit as st
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

"""Wrote this part with the help of ChatGPT and Nominatims offical documentation"""

def get_address_suggestions(query):
    "Function to get address with text input"
    if not query:
        #declaring list
        return []

    # GeoLocater as written in docs of geopy
    geolocator = Nominatim(user_agent="LocatoApp/1.0 (kruskyx24@gmail.com)", timeout=10)

    try:
        # try to get the address results with nominatim using geopy
        location = geolocator.geocode(query, exactly_one=False, addressdetails=True, limit=1)
        if location:
            return [loc.address for loc in location]
        return []

    # error handling
    except GeocoderTimedOut:
        st.error("Error: Geocoding request timed out. Please try again.")
        return
    except Exception as e:
        st.error(f"Error fetching address suggestions: {e}")
        return



