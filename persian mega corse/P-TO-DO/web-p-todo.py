import streamlit as st
import P_functions


st.title("My To DO")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

todos = P_functions.read_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder= "add new todo ...")

