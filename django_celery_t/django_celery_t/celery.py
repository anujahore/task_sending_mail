from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_t.settings')
app = Celery("django_celery_t") #Celery('main') main == project_name

app.conf.enable_utc=False # by default ust timezone set asto
app.conf.update(timezone='Asia/Kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# celery_beat
CELERY_BEAT_SCHEDULE = {
    "send_mail_everyday_at_8": {
        "task": "maninapp.tasks.send_mail_task",
        "schedule": crontab(hour=4, minute=3),
        
    }
    
}

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')