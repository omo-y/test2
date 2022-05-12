import streamlit as st
import numpy as np
import pandas as pd

st.title('フィヨルドの風')

audio_file = open('myaudio.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
