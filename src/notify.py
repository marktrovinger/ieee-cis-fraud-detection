import smtplib
import os
import pandas as pd
import subprocess


def submit_kaggle(df, submission_info, competition, test=False):
    if test == True:
        # test using the sample_submissions.csv file
        bashCommand = "kaggle competitions submit ieee-fraud-detection -f " + \
            os.path.join('submissions', 'sample_submission.csv') + \
            " -m \"Test\" " 
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output, error)
    else:
        df.to_csv(os.path.join('submissions', submission_info+'.csv'))
        bashCommand = "kaggle competitions submit" + competition +  "-f " + \
            os.path.join('submissions', submission_info+'.csv')


def notify(message):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    if (smtpObj.ehlo()[0] != 250):
        print("error contacting gmail smtp")

    smtpObj.starttls()

    smtpObj.login(os.environ.get('EMAIL_ADDRESS'),
                  os.environ.get('APP_PASSWORD'))

    smtpObj.sendmail(os.environ.get('EMAIL_ADDRESS'),
                     os.environ.get('EMAIL_ADDRESS'), message)
