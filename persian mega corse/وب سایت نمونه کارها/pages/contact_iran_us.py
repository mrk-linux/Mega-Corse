import streamlit as st
from send_mail import send_email


st.header("تماس با ما")

with st.form(key = "email_forms"):
    user_email = st.text_input("ادرس ایمل شما")
    rew_message = st.text_area("پیام شما")
    message = f"""/
    subject: New email from{user_email}

    from: {user_email}
    {rew_message}
    """
    button = st.form_submit_button("ارسال")

    if button:
        try:
            send_email(message)
            st.info("ایمل شما ارسال شد")
        except Exception as e:
            st.error(f" ارسال ایمل شکست خورد. Error: {e}")