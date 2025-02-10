import streamlit as st
import time

from streamlit_extras.switch_page_button import switch_page
from AppConfigs.AppConfig import pages

def hero_section(title, description, image=None, imageseq=None, buttonOne=None, buttonTwo=None):
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
                        use = button_config.get("use", "")
                        type = button_config.get("type", None)

                        if use == "switch_page" and function is None:
                            if st.button(label, use_container_width = True, type=f"{type}"):
                                print(f'Switching to {link}')
                                st.switch_page(link)

                        elif use == "function" and callable(function):
                            if st.button(label, use_container_width=True, type=f"{type}"):
                                function()
                                st.write(f"Button '{label}' clicked!")  # Debugging output

            with col4:
                if buttonTwo:
                    for button_config in buttonTwo:
                        label = button_config.get("label", "")
                        function = button_config.get("function", None)
                        link = button_config.get("link", "")
                        use = button_config.get("use", "")
                        type = button_config.get("type", "secondary")

                        if use == "switch_page" and function is None:
                            if st.button(label, use_container_width = True, type=f"{type}"):
                                print(f'Switching to {link}')
                                st.switch_page(link)

                        elif use == "function" and callable(function):
                            if st.button(label, use_container_width=True, type=f"{type}"):
                                function()
                                st.write(f"Button '{label}' clicked!")  # Debugging output

    with col2:
        if image:
            st.image(image, use_container_width=True)

        #if "image_index" not in st.session_state:
        #    st.session_state ["image_index"] = 0  # Start bei erstem Bild

        #def next_image():
        #    """Wechselt zum nächsten Bild in der Sequenz"""
        #    st.session_state ["image_index"] = (st.session_state ["image_index"] + 1) % len(imageseq)
        #    st.rerun()  # Erzwingt ein Neuladen der Seite mit dem neuen Bild

        #if imageseq:
        #    # Aktuelles Bild anzeigen
        #    st.image(imageseq [st.session_state ["image_index"]], use_container_width=True)

            # Nach 15 Sekunden das Bild wechseln
        #    time.sleep(15)
        #    next_image()

