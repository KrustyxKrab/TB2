import streamlit as st

st.title("Information")

st.markdown("""
## 🌍 Welcome to Locato! 

**Thank you for contributing to this community.**  
Wondering what **Locato** is? Here’s everything you need to know!  

---

### 🏡 What is Locato?
Locato is **social media for the real world**—a place to share and save your **favorite locations**, whether it's where you **hang out, eat, drink, or meet friends**.  
**No restrictions!** Any place, anywhere—you decide.

- Moderators will care for a comfortable platform atmosphere.
---

### 🚀 What Does Locato Offer?  

⚠️ **This is a prototype in development**—stay tuned for more features!  

**1. Account Functionality**
- Login & Register Page 

**2. Customize Your Account**
- Personalize your profile  

**3. Manage Your Account Details**
- Edit account settings  

**4. Create a Location**  
- **Unsplash API** – Search for high-quality images  
- **Custom Image Upload** – Use your own pictures  
- **Nominatim API (OpenStreetMap)** – Easily find and save addresses  

**5. Explore Locations**
- Discover new places shared by the community  

**6. Like Locations**
- Show appreciation for places you love  

**7. Your Personal Hub**
- View your **own locations** & **liked locations** anytime  

---

### 🛠️ **Coming Soon**
- **Improved Tagging System** for better recommendations  
- **More Customization Options**  

---
""")

st.title("FAQ")
st.write("Common questions concerning the app!")

expander = st.expander("How can I delete a Location?")
expander.write('''
    At the moment, this part is still under construction. Please wait for the upcoming versions. During this time, the admins will delete not fitting Locations.
''')

expander = st.expander("Does Locato have Moderators?")
expander.write('''
    Yes, Locato has Admins, which care for the quality of the Locations, so it is a Savespace for everyone on this app!
''')

expander = st.expander("How is my data treated?")
expander.write('''
   For me, the founder of Locato, the protection of your data is a very high priority. Due to the early stage of this app, we don't have the best security features, yet all our code is open source and you can see what happens to your data.
    I am also very transparent with your data on the front end. Under **Your Account** you can delete the tags that are used to suggest locations to you or recustomize your account settings
''')

expander = st.expander("Can I help building?")
expander.write('''
   You like the idea of Locato and you want to help? Feel free to contribute by adding as much Locations as you like. If you want to help building the app, please just drop a mail to **kruskyx@gmail.com**
''')


