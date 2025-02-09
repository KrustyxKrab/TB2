import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from AppConfigs.AppConfig import pages

def hero_section(title, description, image, buttonOne=None, buttonTwo=None):
    col1, col2 = st.columns(2)
    with col1:
        if title:
            st.markdown(f"""
            # {title}
            {description}
            """)

            col3, col4 = st.columns(2)

            with col3:
                if buttonOne:
                    for button_config in buttonOne:
                        label = button_config.get("label", "")
                        link = button_config.get("link", "")
                        function = button_config.get("function", None)
                        type = button_config.get("type", "")

                        if type == "switch_page" and function is None:
                            if st.button(label, use_container_width = True, type="primary"):
                                print(f'Switching to {link}')
                                st.switch_page(link)

                        elif type == "function" and callable(function):
                            if st.button(label, use_container_width=True):
                                function()
                                st.write(f"Button '{label}' clicked!")  # Debugging output

            with col4:
                if buttonTwo:
                    for button_config in buttonTwo:
                        label = button_config.get("label", "")
                        function = button_config.get("function", None)
                        link = button_config.get("link", "")
                        type = button_config.get("type", "")

                        if type == "switch_page" and function is None:
                            if st.button(label, use_container_width = True):
                                print(f'Switching to {link}')
                                st.switch_page(link)

                        elif type == "function" and callable(function):
                            if st.button(label, use_container_width=True):
                                function()
                                st.write(f"Button '{label}' clicked!")  # Debugging output

    with col2:
        st.image(image, use_container_width=True)