import streamlit as st
from utils.server.CRUD_Users import write_user_information


def create_card(title, description, id, tags, image=None, additional_info=None):
    """
    Creates a Streamlit card with an optional image, tags, and buttons.
    Includes a 'See More' expander for additional details.
    """
    from utils.tools.generate_id import generate_unique_id
    unique_id = generate_unique_id("random")

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
            st.markdown("**Add to Favorites**")

        with col2:
            # Render buttons if available
            label = "❤"
            button_key = f"{unique_id}_{label}"

            # Check if user data exists in session state
            if st.session_state["user_data"]["username"] is not None:
                #get username and author
                username = st.session_state["user_data"]["username"]
                author = additional_info.get("Author")
                print(author, username)

                DisableBool = username == author if username and author else False

            else:
                DisableBool = True  # Disable the button when not logged in

            # Like Button
            if st.button(label, key = button_key, use_container_width = True, disabled = DisableBool):
                write_user_information(username = st.session_state["user_data"]["username"],
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