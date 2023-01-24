import streamlit as st
import csv
import pandas

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
    df = pandas.read_csv("data.csv", sep=",")

print(df)
leftCol, rightCol = st.columns(2)

for i in range(1, len(data)):
    [title, description, url, image] = data[i]
    if i % 2 == 1:
        with leftCol:
            st.header(title)
            st.image(f"images/{image}")
            st.write(description)
            st.write(url)
    else:
        with rightCol:
            st.header(title)
            st.image(f"images/{image}")
            st.write(description)
            st.write(url)

# using pandas
# for index, row in df.iterrows():
#     if index < 10:
#         with leftCol:
#             st.header(row["title"])
#             st.image(f"images/{row['image']}")
#             st.write(row["description"])
#             st.write(row["url"])
#     else:
#         with rightCol:
#             st.header(row["title"])
#             st.image(f"images/{row['image']}")
#             st.write(row["description"])
#             st.write(row["url"])
