import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/me.jpg", width=600)

with col2:
    st.title("alimrk")
    content = """
    Hi, I'm Ali MRK! I am a Python programmer and I love learning new things.
I am always looking for exciting challenges in the world of programming and enjoy solving real-world problems with code. Python is my main tool,
but my mind is always curious to learn new languages and technologies.
I have worked on various personal and team projects — from building simple automation tools to contributing to open-source projects. 
I believe the best way to learn is by building real things and sharing knowledge with others.
My goal is to use my code to make people's lives a little easier, and along the way, help others learn as well.
    """

    st.info(content)