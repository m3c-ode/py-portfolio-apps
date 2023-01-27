import streamlit as st
import csv
import pandas

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

description = """ 
    Below you can find some of thre apps I have built. Feel free to contact me! 
 """
st.write(description)

with open("./data.csv") as file:
    data = list(csv.reader(file))
    df = pandas.read_csv("data.csv", sep=",")

# print(df)
# passing a list with ratios in arguments, we can control the width of the columns
leftCol, emptyCol, rightCol = st.columns([1.5, 0.5, 1.5])

# for i in range(1, len(data)):
#     [title, description, url, image] = data[i]
#     if i % 2 == 1:
#         with leftCol:
#             st.header(title)
#             st.image(f"images/{image}")
#             st.write(description)
#             st.write(f"[Source Code]({row['url']})")
#     else:
#         with rightCol:
#             st.header(title)
#             st.image(f"images/{image}")
#             st.write(description)
#             st.write(url)

# using pandas
with leftCol:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}")
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with rightCol:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}")
        st.write(row["description"])
        st.write(row["url"])
