import streamlit as st
import functions


st.title("My To DO")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

todos = functions.read_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder= "add new todo ...")

