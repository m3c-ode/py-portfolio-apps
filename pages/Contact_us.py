import streamlit as st
import send_email

st.header("Contact form")

with st.form(key="contactForm"):
    sender = st.text_input("Email: ", placeholder="enter you email address here...")
    message_content = st.text_area(
        "Message: ", placeholder="let me know what you want to share!"
    )

    button = st.form_submit_button("Send")
    if button:
        print("Send email")
        print(sender)
        print(message_content)
        send_email.send_email(sender, message_content)
        st.info("Email sent!")
