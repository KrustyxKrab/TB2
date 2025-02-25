import streamlit as st
import requests

""" Wrote this part with the help of ChatGPT and Nominatims offical documentation"""
def get_address_suggestions(query):
    if not query:
        return []

    # OpenStreetMap Nominatim API URL
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

    # API request parameters
    params = {"q": query, "format": "json", "addressdetails": 1, "limit": 5}

    # Headers (recommended for API usage)
    headers = {"User-Agent": "LocatoApp/1.0 (kruskyx24@gmail.com)"
    }

    try:
        response = requests.get(NOMINATIM_URL, params = params, headers = headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        results = response.json()

        return [result ["display_name"] for result in results]

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching address suggestions: {e}")
        return []