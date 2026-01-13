from Auto_Craft_Main.celery import app
import time
from django.core.management import call_command
from dataentry.utils import send_email_notification
from django.conf import settings

@app.task
def celery_test_task():

    time.sleep(5)

    mail_subject = 'Test Email'
    message = 'This is a Test Email'
    to_email = settings.DEFAULT_TO_EMAIL

    send_email_notification(mail_subject,message,to_email)
    
    return 'Email Sent Successfully.'

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    
    mail_subject = 'Import Data Completed'
    message = 'Your Data import has been successfull. You can use your data now.'
    to_email = settings.DEFAULT_TO_EMAIL

    send_email_notification(mail_subject,message,to_email)

    return 'Data Imported Successfully'