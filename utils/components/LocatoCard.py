import streamlit as st
from utils.server.CRUD_Users import write_user_information

def create_card(title, description, id, tags, image=None, address=None, additional_info=None, buttonLabel = "❤", buttonText= "Add to Favorites" ):
    """
    A Streamlit Card using container to have all the location information in it
    Builds a 'See More' expander for more information
    """
    from utils.tools.generate_id import generate_unique_id
    unique_id = generate_unique_id("random")

    # init variable
    DisableBool = False

    print("init creation of card")

    with st.container(border = True, key = f"card_{unique_id}"):
        if image:
            st.image(image, use_container_width = True)

        tag_str = ", ".join(tags) if isinstance(tags, list) else str(tags)

        st.markdown(f"""
        ##### {title}  
        *{description[0]}*  
        **Tags:**  :blue-background[{tag_str}]
        """, unsafe_allow_html = True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**{buttonText}**")
            print(buttonLabel, buttonText)

        with col2:
            # Render buttons if available
            button_key = f"{unique_id}"

            if buttonText == "Delete":
                print("deletion of location init")
                if st.button(buttonLabel, key = button_key, use_container_width = True):
                    print("delete location")
                    from utils.server.CRUD_Location import deleteLocation
                    deleteLocation("id", id)
                    st.rerun()

            else:
                # Check if user data exists in session state
                if ("user_data" in st.session_state and isinstance(st.session_state ["user_data"],dict) and  # makes sure, user_data is a dictonary for correct usage
                        st.session_state ["user_data"].get("username")  # debugged with chatgpt - error source eliminated
                ):
                    username = st.session_state["user_data"]["username"]
                else:
                    username = None  # Ensure username is always defined

                # if author in additional_info
                author = additional_info.get("Author") if additional_info else None

                # dis- and enabling the button to like the location
                # handle username & author
                if username and author:
                    DisableBool = username == author  # disable if the user is the author
                else:
                    DisableBool = True  # disable if user is not logged in

                # Like Button
                if st.button(buttonLabel, key = button_key, use_container_width = True, disabled = DisableBool):
                    write_user_information(username = username,
                        type = "array", key = "Likes", value = id)

            if DisableBool is True:
                if username == author and username and author:
                    st.info("Can't Like own locations")

                else:
                    st.info("Log-In to Like")

        with st.expander(f"Read More"):
            st.markdown(f"*{description[1]}*")
            if additional_info:
                st.write("---")
                st.write(address)
                for key, value in additional_info.items():
                    st.write(f"**{key}:** {value}")

# Custom styling
st.markdown("""
<style>
/* Style Streamlit containers */
div[data-testid="stContainer"] {
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
}

/* Improve spacing between components */
[data-testid="stVerticalBlock"] > div {
    padding: 5px;
}
</style>
""", unsafe_allow_html = True)