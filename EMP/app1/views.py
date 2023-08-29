from django.shortcuts import render, HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.




from app1.models import TestingEmp
from datetime import date
from app1.tasks import test_demo, send_mail_bday_wanni
from rest_framework.decorators import api_view

# testing a view
def emp_birthday(request):
    all_emps = TestingEmp.objects.all()
    for single_emp in all_emps:
        if single_emp.birthdate.day == date.today().day and single_emp.birthdate.month == date.today().month:
            print("happy birthday:- ",single_emp)
        if single_emp.Date_joined.day == date.today().day and single_emp.Date_joined.month == date.today().month:
            work_years = date.today().year - single_emp.Date_joined.year
            print(f"happy {work_years} years work anniversory:- ",single_emp)
        
    return HttpResponse("doneeeeeee")

@api_view()
def sending_wishes(req):
    send_mail_bday_wanni.delay()
    return HttpResponse("emails send successfully......!!!")


def wishes_scheduler_dynamic(request):
    sceduler, created = CrontabSchedule.objects.get_or_create(hour=16, minute=40)
    tasks = PeriodicTask.objects.create(crontab=sceduler, name="wishes_sending_at_16", task="app1.tasks.send_mail_bday_wanni")
    return HttpResponse("doen sneding.............")


def test_cel(req):
    test_demo.delay()
    return HttpResponse("done testing...........!!!!")