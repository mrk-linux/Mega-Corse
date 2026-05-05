import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/me.jpg")

with col2:
    st.title("alimrk")
    content = """
سلام، من alimrk هستم! برنامه‌نویس پایتون و عاشق یادگیری چیزهای جدید.
من همیشه به دنبال چالش‌های جذاب در دنیای برنامه‌نویسی هستم و از حل مسائل واقعی با کدنویسی لذت می‌برم.
پایتون ابزار اصلی من است، اما ذهنم همیشه کنجکاو یادگیری زبان‌ها و فناوری‌های جدید است.
با پروژه‌های شخصی و تیمی مختلفی کار کرده‌ام؛ از ساخت ابزارهای خودکارسازی ساده تا مشارکت در پروژه‌های متن‌باز.
ایمان دارم که بهترین راه برای یادگیری، ساختن چیزهای واقعی و اشتراک دانش با دیگران است.
هدف من این است که بتوانم با کدهایم، حتی اندکی، زندگی دیگران را آسان‌تر کنم و در مسیر یادگیری، دیگران را نیز همراه کنم.
    """

st.info(content)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep= ";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])