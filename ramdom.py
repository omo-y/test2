import streamlit as st
import numpy as np

st.title('ランダムサンプル')
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)