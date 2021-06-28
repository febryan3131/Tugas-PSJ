#!/usr/bin/env python3
# Listing 1 – First email client
import smtplib
import getpass
import os

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # ssl port 465, tls port 587

def send_email(sender, recipient):
        """ Send email message """
        msg = MIMEMultipart()
        msg['To'] = recipient
        msg['From'] = sender
        subject = input('Enter your email subject: ')
        msg['Subject'] = subject
        message = input('Enter your email message. Press Enter when finished. ')
        part = MIMEText('text', "plain")
        part.set_payload(message)
        msg.attach(part)
	# attach an image in the current directory
        filename = input('Enter the file name of a JPG image: ')
        path = os.path.join(os.getcwd(), filename)
        if os.path.exists(path):
                img = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
                img.add_header('Content-Disposition', 'attachment',filename=filename)
                msg.attach(img)

        # create smtp session
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.set_debuglevel(1)
        session.starttls()
        session.ehlo
        password = getpass.getpass(prompt="Enter you email password:")
        # login to server
        session.login(sender, password)
        # send mail
        session.sendmail(sender, recipient, msg.as_string())
        print("You email is sent to {0}.".format(recipient))
        session.quit()

if __name__ == '__main__':
        sender = input("Enter sender email address: ")
        recipient = input("Enter recipient email address: ")
        send_email(sender, recipient)

