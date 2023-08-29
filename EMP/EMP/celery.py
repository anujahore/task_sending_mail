

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab





os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMP.settings')
app = Celery("EMP") #Celery('main') main == project_name

app.conf.enable_utc = False # by default ust timezone set asto
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')


app.conf.beat_scheduler = {
        "wishes_send_11am(IST)": {
        "task": "app1.tasks.send_mail_bday_wanni",
        "schedule": crontab(hour=23, minute=43)
    }
}

# CELERY_BEAT_SCHEDULER = {
#     "wishes_send_11am(IST)": {
#         "task": "app1.tasks.send_mail_bday_wanni",
#         "scedule": crontab(hour=4, minute=22)
#     }
# }


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')