import streamlit as st


def create_card(title, description, id, tags, image=None, additional_info=None):
    """
    Creates a Streamlit card with an optional image, tags, and buttons.
    Includes a 'See More' expander for additional details.
    """
    with st.container(border = True, key = f"card_{id}"):
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
            button_key = f"{id}_{label}"

            if st.button(label, key = button_key, use_container_width=True):
                st.write(f"Liked")  # Debugging output

        # "See More" Expander instead of Popup
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