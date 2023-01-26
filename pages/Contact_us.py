import streamlit as st

st.header("Contact form")

with st.form(key="contactForm"):
    email = st.text_input("Email: ", placeholder="enter you email address here...")
    message = st.text_input(
        "Message: ", placeholder="let me know what you want to share!"
    )
    button = st.form_submit_button("Send")
    if button:
        print("Send email")
