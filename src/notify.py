import smtplib
import os


def submit_kaggle():
    pass

def notify(message):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    
    if (smtpObj.ehlo()[0] != 250):
        print("error contacting gmail smtp")

    smtpObj.starttls()

    smtpObj.login(os.environ.get('EMAIL_ADDRESS'), os.environ.get('APP_PASSWORD'))

    smtpObj.sendmail(os.environ.get('EMAIL_ADDRESS'), os.environ.get('EMAIL_ADDRESS'), message)