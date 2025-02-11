import streamlit as st
import requests
from src.poi_list import poi_tags
from utils.server.CRUD_Location import create_location
from utils.tools.generate_id import generate_unique_id

st.title("Create a Location. Now.")
st.write("We are happy, you are contributing to our community 🎉")

#title, town, desc, tags, image, author, rating, comments

def suggest_tags(user_input, poi_tags):
    """Suggests tags based on user input by filtering matching tag names."""
    user_input = user_input.lower().strip()
    suggestions = {k: v for k, v in poi_tags.items() if user_input in v.lower()}

    return suggestions


create_placeholder = st.container(border = True)
after_creation = st.container(border = True)


with create_placeholder:
    st.markdown("#### 📌 Title of Your Location")
    st.markdown("Give your location a unique and catchy title to attract attention!")
    title = st.text_input(label = "Enter a title...")

    st.markdown("#### 📸 Search for a picture")
    st.markdown("Search for a fitting image of the location")
    link = st.text_input("Search for an image")
    # Replace with your Unsplash API key
    api_key = st.secrets['unsplash_api_key']

    def get_images(query, api_key, results=1):
        """Code from chatgpt to fetch image URLs based on a query."""
        search_url = "https://api.unsplash.com/search/photos"
        response = requests.get(search_url,
                                params = {"query": query.lower(), "client_id": api_key, "per_page": results})
        return [img["urls"]["regular"] for img in response.json().get("results", [])]


    if link:
        images = get_images(link, api_key, results = 1)
        for img_url in images:
            st.image(img_url, caption = link.title(), use_container_width = True)

    st.markdown("#### 📍 Where is Your Location?")
    st.markdown("Specify the city or town where your location is situated.")
    town = st.text_input(label = "Enter town or city...")

    st.markdown("#### ✏️ Short Description")
    st.markdown("Provide a **one-liner** about your location. This is the first impression!")
    short_desc = st.text_input(label = "Write a short description...")

    st.markdown("#### 📝 Detailed Description")
    st.markdown("Give visitors a more **in-depth** look into what makes this place special.")
    desc = st.text_area(label = "Write a detailed description...")

    st.markdown("#### 🔍 Pick Tags That Fit")
    st.markdown("Search for relevant **categories** to make your location easier to find.")
    tag_try = st.text_input(label = "🔍 Search for tags...", placeholder = "Type keywords like 'Cafe', 'Museum'...")

    if tag_try:
        matching_tags = suggest_tags(tag_try, poi_tags)

        if matching_tags:
            st.markdown("###### 🔖 Suggested Tags:")

            # ✅ Extract matching tag IDs
            tag_options = list(matching_tags.keys())

            # ✅ Show readable tag names, but store numeric tag IDs
            tags = st.pills(label = "Tags", options = tag_options, format_func = lambda tag: poi_tags[tag])

            # ✅ Show stored numeric tag values
            st.write("Selected Tag IDs:", tags)

        else:
            st.warning("⚠️ No matching tags found. Try another word.")

    username = st.session_state['user_data']['username']
    st.write(f"Create Location as {username}")

    colA, colB = st.columns(2)
    with colA:
        save = st.button(label = "Save Location", type = "primary", use_container_width = True)

        if save:
            unique_id = generate_unique_id(type = "location")
            create_location(title, town, desc = [short_desc, desc], tags = tags, image = img_url, author = username, id = unique_id)
            create_placeholder.empty()

            with after_creation:
                st.success("Location successfully created")


    with colB:
        cancel = st.button(label = "Cancel", type = "secondary", use_container_width = True)
        if cancel:
            st.switch_page("pages/Explore.py")
