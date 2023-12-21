import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Sergio Galindo Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width = 200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** Sergio Galindo")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Sergio Galindo""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "Sergio.jpg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Master student in Big Data & Analytics"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a cyber criminologist doing my master's degree in Big data and analytics

- 🛩️ Previous experience: I worked on sales and IT team for EnergyBox, as a Cyber Criminology analyst for the Bolivian police, and information security and cyber security for Banco Nacional de Bolivia

- ❤️ My biggest passion is traveling around the world and learning about different cultures 

- 🤖 My personal goals are to work with banking and at some point have my own company with a focus on data analysis

- 🏂 My hobbies are: Tennis, Horse riding, food

- 📫 sergio_galindo29@hotmail.com

- 🏠 Barcelona Spain
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc
