import streamlit as st

st.set_page_config(layout="wide")

st.title("Portfolio Website")
col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg", width=300)

with col2:
    st.title("Maxime Maréchal-McCoy")
    content = """ 
     Hi, this is Maxime. Lorem ipsum blablabla
       """
    st.info(content)
