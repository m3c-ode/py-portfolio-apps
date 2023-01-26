import smtplib, ssl

# parameters for stmplib
host = "smtp.gmail.com"
port = 465

password = "jyfbvhrjpkwvbutg"
username = "maxime.marechalmccoy@gmail.com"
receiver = "maxime.marechalmccoy@gmail.com"

message = """\
Subject: Test from python script
Test message to send
 """

# context to create security
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
