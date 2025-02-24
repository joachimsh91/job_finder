'''Email module'''

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from data import MAIL_ADDRESS, MAIL_PASSWORD

def send_mail():
    '''Sends an email'''
    msg = MIMEMultipart()
    body_part = MIMEText('Here is the latest job listings', 'plain')
    msg['Subject'] = 'Jobs'
    msg['From'] = MAIL_ADDRESS[0]
    msg['To'] = MAIL_ADDRESS[1]

    msg.attach(body_part)

    with open(r'C:\Users\Joach\repos\job_finder\files\jobs', 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name='Job listings'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MAIL_ADDRESS[0], MAIL_PASSWORD[0])
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print('An email with job listings was sent to your email address')
    server.quit()
