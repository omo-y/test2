import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('蝶の表示')

img=Image.open('23809287_s-1.jpg')
st.image(img,caption='butterfly',use_column_width=True)