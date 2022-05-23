import streamlit as st
import pandas as pd
st.title('はじめての表')
st.text('インタラクティブな表示の作成2行2列')
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df