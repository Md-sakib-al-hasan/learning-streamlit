import streamlit as st
st.title("Streamlit Widgets :input Element")
st.divider()

# Text input
name = st.text_input("What is your name? :house:")
number= st.number_input("Enter your age")
st.write("Hello", name)
st.write("You are", number, "years old")
