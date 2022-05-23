import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name