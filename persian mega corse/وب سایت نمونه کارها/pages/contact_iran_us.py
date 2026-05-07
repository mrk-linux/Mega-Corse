import streamlit as st

st.header("تماس با ما")

with st.form(key = "email_forms"):
    user_email = st.text_input("ادرس ایمل شما")
    message = st.text_area("پیام شما")
    button = st.form_submit_button("ارسال")

    if button:
        pass