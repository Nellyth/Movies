from celery import shared_task, chord
from django.contrib.auth.models import User
from django.core.management import call_command

from apps.movies.models import Suggestion
from movie_project import settings
from django.core.mail import send_mail


@shared_task()
def query_movies(data: str) -> str:
    result = call_command('download', '-s', data)
    return result


@shared_task
def send_email(data: str, **kwargs) -> str:
    affair = 'Finished Movie Filter'
    message = 'The search for movies has finished. \n' \
              'the films added were: {}'.format(data)
    send_mail(affair, message, settings.EMAIL_HOST_USER, [kwargs.get('user').get('email')], fail_silently=False)
    Suggestion.objects.all().delete()
    return 'The mail was sent correctly to the user: {}'.format(kwargs.get('user').get('username'))


@shared_task
def suggestion():
    data = Suggestion.objects.all()
    if data:
        for suggests in data:
            user = {'username': suggests.user.username, 'email': suggests.user.email}
            chord(query_movies.s(suggests.name))(send_email.s(user=user))

    """
    if len(data) > 1:
        callback = send_email.s(user=user)
        header = [query_movies.s(mov.name) for mov in data]
        chord(header)(callback)
    elif len(data) == 1:
        chord(query_movies.s(data.first().name))(send_email.s(user=user))
    """
    return 'Search for suggestions completed'
