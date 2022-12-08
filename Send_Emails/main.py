from dotenv import load_dotenv
from decouple import config
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv() # take environment variables from .env.

# Define the elements of the email
email_sender = config('EMAIL_SENDER') 
email_password = config('EMAIL_PASSWORD')
#email_receiver = 'email@example.com'
email_receiver = 'isa_olmedo14@outlook.es'

subject = 'Keep working on your portafolio!'
body = """
You can do it!
"""

email = EmailMessage() # Object to write the email
# Email elements
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

# Layer of security (SSL) to keep a secure internet conection
context = ssl.create_default_context()

# Create a object SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Autentication
    smtp.login(email_sender, email_password) # Login
    # Send email
    smtp.sendmail(email_sender, email_receiver, email.as_string())
    # Close session
    smtp.quit()