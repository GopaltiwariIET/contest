from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib

to_address = 'gopaltiwari28122003@gmail.com'
from_address = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')
print(os.getenv('EMAIL_USER'))
# Function to send email
def send_email(subject, body, to_address):
    # Create a MIMEText message object
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    # Attach the body to the message
    body_text = MIMEText(body, 'plain')
    msg.attach(body_text)

    # Use SMTP_SSL to connect to Gmail's server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())

    print(f'Email sent to {to_address}')
