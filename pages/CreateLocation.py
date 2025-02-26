import streamlit as st
import requests
import time
from src.poi_list import poi_tags
from utils.server.CRUD_Location import create_location
from utils.tools.generate_id import generate_unique_id
from utils.tools.address_suggestion import get_address_suggestions

st.title("Create a Location. Now.")
st.write("We are happy, you are contributing to our community 🎉")

def suggest_tags(user_input, poi_tags):
    """Suggests tags based on user input by filtering matching tag names."""
    user_input = user_input.lower().strip()
    suggestions = {k: v for k, v in poi_tags.items() if user_input in v.lower()}

    return suggestions


if "DisableButton" not in st.session_state or st.session_state["DisableButton"] is None:
    st.session_state["DisableButton"] = False

if "selected_address" not in st.session_state:
    st.session_state["selected_address"] = ""

create_placeholder = st.container(border = True)
after_creation = st.container(border = True)


with create_placeholder:
    st.markdown("#### 📌 Title of Your Location")
    st.markdown("Give your location a unique and catchy title to attract attention!")
    title = st.text_input(label = "Enter a title...")

    st.markdown("#### 📸 Search for a picture")
    st.markdown("Upload or Search for a fitting image of the location")

    image_upload = st.file_uploader(label="Image", type=['png', 'jpg', 'JPEG'], accept_multiple_files=False)

    img_data = None
    # code from streamlit.io
    if image_upload is not None:
        # Read the image file as binary
        image_binary = image_upload.getvalue()

        if image_binary:
            st.session_state["DisableButton"] = True
            img_data = image_binary  # Assign binary data to img_data

    link = st.text_input("Search for an image", disabled=st.session_state["DisableButton"])
    # Replace with your Unsplash API key
    api_key = st.secrets['unsplash_api_key']


    # ChatGPT helped me with this code...
    def get_image(query, api_key, results=1):
        """Code from chatgpt to fetch image URLs based on a query."""
        search_url = "https://api.unsplash.com/search/photos"
        response = requests.get(search_url,
                                params = {"query": query.lower(), "client_id": api_key, "per_page": results})
        return [img["urls"]["regular"] for img in response.json().get("results", [])]


    if link:
        images = get_image(link, api_key, results = 1)
        if images:
            img_data = images[0]
            st.image(img_data, caption = link.title(), use_container_width = True)


    # ==================

    # Streamlit UI
    st.markdown("#### 📍 Address")
    query = st.text_input("Enter a location or address", "")
    search = st.button("Search for Address", type = "secondary")

    if search:
        results = get_address_suggestions(query)
    if results:
        st.session_state["selected_address"] = results[0]
        st.success(f"Selected Address: {st.session_state["selected_address"]}")

    else:
        st.warning("No suggestions found. Try another address.")


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

            tag_options = list(matching_tags.keys())

            tags = st.pills(label = "Tags", options = tag_options, format_func = lambda tag: poi_tags[tag])

        else:
            st.warning("⚠️ No matching tags found. Try another word.")

    username = st.session_state['user_data']['username']
    st.markdown(f"""Create Location as **{username}**""")

    colA, colB = st.columns(2)
    with colA:
        save = st.button(label = "Save Location", type = "primary", use_container_width = True)

        if save:
            if title and st.session_state["selected_address"] and tags and short_desc:
                unique_id = generate_unique_id(type = "location")
                create_location(title, desc = [short_desc, desc], tags = tags,  image = img_data, address = st.session_state["selected_address"], author = username, id = unique_id)

                with after_creation:
                    st.success("Location successfully created")

                time.sleep(2)
                st.switch_page("pages/Explore.py")

            else:
                st.error("Please fill out the mandatory inputs or cancel creation.")

    with colB:
        cancel = st.button(label = "Cancel", type = "secondary", use_container_width = True)
        if cancel:
            st.switch_page("pages/Explore.py")
