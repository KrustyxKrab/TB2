import streamlit as st

st.markdown("""
# Project Documentation

# Locato App  
## Tech Basics II Project  

---

## Abstract  
Locato is an App as Social Media for real-life locations. This means that it is a platform model where users can insert and view different locations of other users. This Project Report presents the major parts of the development process of the App, including the key challenges, limitations, and test user experiences.  

---

## Development Process  

The development of the **Locato App** can be split into different stages. These stages differ not only in tasks but also in the level of detail. During the later stages of development, I focused on details, whereas, in the initial stages, I only coded the minimal functional structure.  

### **Development Stages:**  
1. **Ideation**  
2. **Drafting**  
3. **Minimal Functional Structure**  
4. **Design**  
5. **Adding Features**  
6. **Testing**  
7. **Debugging and Iteration**  

---

## 1. Ideation  

During the preparations for my pitch in the lecture, I gathered ideas on how to evolve my app in the second project period. Initially, I felt challenged and a bit limited with **Streamlit**, but this changed as the process progressed.  

Nevertheless, I started working on my key ideas and goals within the given boundaries.  

### **Key Goals:**  
- Build an app that runs reliably  
- Establish a clear and modular project structure  
- Focus on the algorithms that suggest locations  
- Design a beautifully structured app  
- Emphasize the **back-end**  

---

## 2. Drafting  

In the drafting process, I laid the foundation for achieving my goals (see **Attachments: 1.0 Drafting**). During this phase, I focused on the necessary scripts and functions and how to structure them.  

I applied my experience from past web design projects to keep scripts as simple as possible, making debugging and error-fixing easier.  

---

## 3. Minimal Functional Structure  

Once the first simple design was complete, I set up the environment, including:  
- Folder structure  
- GitHub repository  

### **Key Challenges:**  
One of the main challenges I faced was **Streamlit’s navigation system**. Initially, I added a `pages/` folder in the structure but later discovered that Streamlit provides a built-in navigation system for this.  

However, I wanted to manipulate navigation based on **user roles (admin or not)** and **user status (logged in or not)**.  

#### **Solution:**  
- After researching Streamlit, I found **multipage apps** and **st.navigation**.  
- I changed my entry point from `main.py` to an **upstream script** called **`BuildApp.py`**, where all other pages are nested.  

This technique led to the next challenge.  

---

## 4. Design  

Due to the use of `BuildApp.py` and nested scripts, **individual `st.page.config` no longer worked**. This disabled functions like:  
- **Wide-page layout**  
- **Default Streamlit layout**  

### **Solution:**  
I implemented a **CSS-based solution** to imitate the function.  

### **Design Decisions:**  
- The app follows a **minimalistic design**  
- **Streamlit’s default colors** were replaced  
- Added **images and emojis** for better visual impact  

---

## 5. Adding Features  

At this stage, I integrated various features, including those learned in class and additional custom features.  

### **Key Features:**  
- **Unsplash API** → Integrated image search  
- **Nominatim API (OpenStreetMap API)** → Implemented location search functionality  

### **Challenges with Nominatim API:**  
- The implementation was harder than expected.  
- Incorrect usage caused **IP blocking issues**.  
- Despite the difficulties, the API **significantly enhanced** the platform.  

### **Admin Rights:**  
- I enjoyed implementing **admin rights** into the app.  
- I find it interesting and useful to have an **admin dashboard**.  
- This aligns with my **goal of focusing on the back-end**.  

### **Algorithm Challenge:**  
- Initially, I aimed to develop a **location suggestion algorithm**.  
- Due to **time constraints**, I couldn’t focus on this.  
- The current system **suggests locations based on tags stored in user data**.  

---

## 6. Testing  

During the testing phase, I collected **user feedback** from early testers.  

### **General Feedback:**  
- **Positive overall reception**  
- **UX improvement:** A tester pointed out **inconveniences** in location creation.  
  - **Solution:** Improved user-friendliness.  

### **Nominatim API Issues:**  
- During testing, **the app URL (locato.streamlit.app) was blocked** due to API request errors.  
- I worked extensively on fixing this issue and **hope it won’t reoccur**.  

### **Biggest Challenge Identified by Testers:**  
- **User-generated content**: The app’s value depends on user participation.  
- **Solution:**  
  - I added **many starting locations** to encourage engagement.  
  - I hope fellow **digital media students** will test and contribute.  

---

## 7. Debugging and Iteration  

While cleaning up the code and improving efficiency, I encountered:  
- **Minor and major bugs**  
- **Tester-reported issues**  

### **Final Focus Areas:**  
- Fixed reported **bugs**  
- Ensured the app is **fully functional and user-friendly**  

---

## **Conclusion**  

The **Locato App** is a **social media platform for real-life locations**, aiming to enhance user experience through structured development and feature integration. Despite challenges, especially with **Streamlit navigation and the Nominatim API**, the project evolved successfully.  

Further improvements, particularly in the **location suggestion algorithm** and **user engagement**, will enhance the app’s potential in the future.  

""")