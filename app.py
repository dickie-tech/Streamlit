import streamlit as st

st.title("🚀 My First Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    st.success(f"Hello {name}! Welcome to Streamlit 🎉")

st.write("This app demonstrates a basic Streamlit GUI.")
