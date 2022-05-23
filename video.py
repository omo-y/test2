import streamlit as st
import numpy as np
import pandas as pd

st.title('星空の風景')

video_file = open('myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes,start_time=0)