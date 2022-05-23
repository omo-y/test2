import streamlit as st
x = st.slider('x',0,100,50)  # 👈 this is a widget
st.write(x, 'squared is', x * x)