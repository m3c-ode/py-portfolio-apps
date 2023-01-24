import streamlit as st
import csv

# st.set_page_config(layout="wide")

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

description = """ 
    Below you can find some of thre apps I have built. Feel free to contact me! 
 """
st.write(description)

with open("./data.csv") as file:
    data = list(csv.reader(file))

leftCol, rightCol = st.columns(2)

for i in range(1, len(data)):
    [title, description, url, image] = data[i]
    if i % 2 == 1:
        with leftCol:
            st.title(title)
            st.write(description)
            st.write(url)
            st.write(image)
    else:
        with rightCol:
            st.title(title)
            st.write(description)
            st.write(url)
            st.write(image)

# with leftCol:
#     # [title, description, url, image] = [
#     #     project for index, project in enumerate(data) if index % 2 == 0
#     # ]
#     i = 1
#     for i in range(len(data)):
#         if i % 2 == 1:
#             [title, description, url, image] = data[i]
#             st.title(title)
#             st.write(description)
#             st.write(url)
#             st.write(image)


# with rightCol:
#     st.title("cCol 2")
