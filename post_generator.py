# post_generator.py

import os
import smtplib
from email.mime.text import MIMEText

post = """
Today's LinkedIn Post
AI is transforming modern Java applications...
#Java #AI
"""

msg = MIMEText(post)

msg["Subject"] = "LinkedIn Post Draft"
msg["From"] = "media.agent26@gmail.com"
msg["To"] = "media.agent26@gmail.com"

email_user = os.environ["EMAIL_USER"]
email_password = os.environ["EMAIL_PASSWORD"]

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_user, email_password)
server.send_message(msg)
server.quit()

