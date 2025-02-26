from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

""" Wrote this part with the help of ChatGPT and Nominatims offical documentation"""

def get_address_suggestions(query):
    if not query:
        return []

    # GeoLocater as written in docs of geopy
    geolocator = Nominatim(user_agent="LocatoApp/1.0 (kruskyx24@gmail.com)", timeout=10)

    try:
        location = geolocator.geocode(query, exactly_one=False, addressdetails=True, limit=1)
        if location:
            return [loc.address for loc in location]
        return []

    except GeocoderTimedOut:
        return ["Error: Geocoding request timed out. Please try again."]
    except Exception as e:
        return [f"Error fetching address suggestions: {e}"]



