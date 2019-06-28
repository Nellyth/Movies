from celery import shared_task
from django.core.management import call_command
from movie_project import settings
from django.core.mail import send_mail


@shared_task()
def query_movies(data):
    result = call_command('download', '-s', data)
    return result


@shared_task
def send_email(data, **kwargs):
    affair = 'Finished Movie Filter'
    message = 'The search for movies has finished. \n' \
              'the films added were: {}'.format(data)
    send_mail(affair, message, settings.EMAIL_HOST_USER, [kwargs.get('user').get('email')], fail_silently=False)
    return 'The mail was sent correctly to the user: {}'.format(kwargs.get('user').get('username'))


@shared_task
def sum_result(x):
    return x
