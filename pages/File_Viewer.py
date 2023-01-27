import streamlit as st
import pandas

st.header("File viewer")

upload = st.file_uploader("Click below to select your .csv or .xlsx file")

if upload:
    print(upload)
    if ".xlsx" in upload.name:
        print("It's an excel file")
    try:
        df = pandas.read_csv(upload)
        st.write(df)
    except UnicodeDecodeError:
        df = pandas.read_excel(upload)
        st.write(df)
