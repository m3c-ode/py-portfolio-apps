import smtplib, ssl

# parameters for stmplib
def send_email(sender, message_content):
    host = "smtp.gmail.com"
    port = 465

    password = "jyfbvhrjpkwvbutg"
    username = "maxime.marechalmccoy@gmail.com"
    recipient = "maxime.marechalmccoy@gmail.com"

    # needs to be properly indented as such to be able to get subejct and From
    message = f"""\
Subject: Enquiry from portfolio

From: {sender}
{message_content}
"""

    # context to create security
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recipient, message)
