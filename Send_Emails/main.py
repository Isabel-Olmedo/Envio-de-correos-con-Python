from dotenv import load_dotenv
from decouple import config
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv() # take environment variables from .env.

# Define the elements of the email
sender_email_address = config('EMAIL_SENDER') 
sender_email_password = config('EMAIL_PASSWORD')
receiver_email_address = 'email@example.com'

email_subject = 'Keep working on your portafolio!'
email_body = "You can do it! "

# Create an email message object to write the email
email = EmailMessage() 

# Configure email elements
email['From'] = sender_email_address
email['To'] = receiver_email_address
email['Subject'] = email_subject
# Set email body text 
email.set_content(email_body)

# Layer of security (SSL) to keep a secure internet conection
context = ssl.create_default_context()

# Set smtp server and port
server_email_smtp = 'smtp.gmail.com'
smtp_port = 465

with smtplib.SMTP_SSL(server_email_smtp, smtp_port, context=context) as smtp: # Create a object SMTP
    # Autentication
    smtp.login(sender_email_address, sender_email_password) # Login
    # Send email
    smtp.sendmail(sender_email_address, receiver_email_address, email.as_string())
    # Close connection to server 
    smtp.quit()
