import streamlit as st
import numpy as np
import pandas as pd

st.title('テーブルメソッド利用')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)