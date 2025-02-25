import streamlit as st
import requests
import time

""" Wrote this part with the help of ChatGPT and Nominatims offical documentation"""


def get_address_suggestions(query):
    if not query:
        return []

    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    params = {"q": query, "format": "json", "addressdetails": 1, "limit": 5}
    headers = {"User-Agent": "LocatoApp/1.0 (kruskyx24@gmail.com)"}

    try:
        time.sleep(1)  # Add a delay to avoid rate limiting
        response = requests.get(NOMINATIM_URL, params = params, headers = headers, timeout = 10)
        response.raise_for_status()
        results = response.json()
        return [result ["display_name"] for result in results]

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching address suggestions: {e}")
        return []


