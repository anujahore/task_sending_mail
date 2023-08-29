from django.shortcuts import render, HttpResponse

# Create your views here.

from .tasks import demo_task, send_mail_task

def send_mail_to_all(request):
    send_mail_task.delay()
    return HttpResponse("mail hase been successfully...!!!")


def test(request):
    demo_task.delay()
    return HttpResponse("donedwwew")


from mainapp.models import TestingEmp
from datetime import date

def emp_birthday(request):
    all_emps = TestingEmp.objects.all()
    for single_emp in all_emps:
        if single_emp.birthdate.day == date.today().day and single_emp.birthdate.month == date.today().month:
            print(single_emp)
        if single_emp.Date_joined.day == date.today().day and single_emp.Date_joined.month == date.today().month:
            print(single_emp)
        
    return HttpResponse("doneeeeeee")

