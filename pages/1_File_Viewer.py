import streamlit as st
import pandas

st.title("File viewer")
st.subheader(
    "App to visualize different data files (currently .xlsx and .csv are supported)"
)

upload = st.file_uploader(
    """ 
Clickez le bouton ci-dessous pour télécharger votre fichier .csv ou .xlsx à visionner.\n
Click below to select your .csv or .xlsx file 
"""
)

if upload:
    print(upload)
    print(type(upload))
    if ".xlsx" in upload.name:
        print("It's an excel file")
    try:
        df = pandas.read_csv(upload)
        st.write(df)
    except UnicodeDecodeError:
        df = pandas.read_excel(upload)
        st.write(df)
