import smtplib
import os 

from dotenv import load_dotenv

load_dotenv('.env')
gmail_user = os.environ.get("gmail_user")
gmail_pwd = os.environ.get("gmail_pwd")

def send_email(subject, msg, to, gmail_user, gmail_pwd):
    """2
    Send an email using the smtplib library.

    Parameters
    ----------
    subject : str
        The subject of the email.
    msg : str
        The message body of the email.
    to : str
        The recipient of the email.
    gmail_user : str
        The Gmail username.
    gmail_pwd : str
        The Gmail password.
    """
    try:
        # Create a secure SSL context
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        # Log in to the Gmail server
        server.login(gmail_user, gmail_pwd)

        # Create the message
        message = 'Subject: {}\n\n{}'.format(subject, msg)

        # Send the email and log out
        server.sendmail(gmail_user, to, message)
        server.quit()
        
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send.")
        print(e)

subject = "Test Subject "
msg = "Hello there, this is a test email from python."
# to = "recipient@example.com"

if __name__ == "__main__":
    send_email(subject, msg, to, gmail_user, gmail_pwd)
    
