import streamlit as st
st.title('Layout')
button =st.checkbox('Layout')
if button:
    expander1=st.expander('問い合わせ１')
    expander1.write('問い合わせ１の回答１')
    expander2=st.expander('問い合わせ２')
    expander2.write('問い合わせ１の回答２')
    expander3=st.expander('問い合わせ３')
    expander3.write('問い合わせ１の回答３')