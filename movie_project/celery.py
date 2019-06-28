import os
from celery import Celery
from celery.schedules import crontab

name = 'movie_project'
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings'.format(name))

app = Celery(name, backend='amqp://guest:guest@localhost:5672//', )

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'execute-the-indicated-task-every-5-minutes': {
        'task': 'apps.movies.tasks.suggestion',
        'args': (),
        'schedule': crontab(minute='*/5'),
    },
}
app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
