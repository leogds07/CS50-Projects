#IMPORTS
import sys
from generate_email import generate_emails
import smtplib
from get_info import get_email, get_pwd
from handle_password import load_key, decrypt_message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from get_emails_hotels import get_emails_hotels
import os

#SETTINGS
hotels, receiver_emails = get_emails_hotels()
messages: list = generate_emails()
sender_email = get_email()
subject = 'Booking Request'
encrypted_password = get_pwd()

# Decrypt password
key = load_key()
pwd = decrypt_message(encrypted_password, key)

def send_emails():
    # Start server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # TLS = Transport Layer Security

    # Try to log in
    try:
        server.login(sender_email, pwd)
        print('Logged in...')
    except smtplib.SMTPAuthenticationError:
        sys.exit('Unable to sign in')

    i = 1  # To keep track of the index

    #if len(messages) == len(receiver_emails):
    for message_body, receiver in zip(messages, receiver_emails):
        # Create MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the message body with UTF-8 encoding
        msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

        try:
            # Send the email
            server.sendmail(sender_email, receiver, msg.as_string())
            print(f'Email n.{i} sent!')
            i += 1
        except smtplib.SMTPException as e:
            print(f"Failed to send email to {receiver}: {str(e)}")

    # Close the server connection
    server.quit()

    #all completed successfully
    print('Process Completed!')