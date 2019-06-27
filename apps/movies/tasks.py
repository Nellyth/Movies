import json
import smtplib
from celery import shared_task
from movie_project import settings
from django.core.management import call_command
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@shared_task
def command_send_emails_users(data):
    call_command('download', '-s', data['movie'])
    affair = 'Test Message'
    message = 'This is an email sent for the purpose of understanding how the Celery Library works'
    send_email.delay(data)


@shared_task
def send_email(data):
    email = settings.email
    password = settings.password
    send_to_email = data.get('email')
    subject = 'Finished Movie Filter'
    message = 'The search for movies has finished.'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(json.dumps(message), 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    return 'The mail was sent correctly to the user: {}'.format(data.get('username'))
