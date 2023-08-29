

from celery import shared_task
from app1.models import TestingEmp
# from django.conf import settings
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.core.mail import send_mail

from datetime import date
from django.core.mail import send_mail
from EMP.settings import EMAIL_HOST_USER

@shared_task(bind=True)
def test_demo(self):
    for i in range(10):
        print(i)
    return "done testing successfully...!"

@shared_task(bind=True,name="wishes_send_11am(IST)")
def send_mail_bday_wanni(self):
    all_emps = TestingEmp.objects.all()
    for single_emp in all_emps:
        if single_emp.birthdate.day == date.today().day and single_emp.birthdate.month == date.today().month:
            print("happy birthday:- ",single_emp)
            
            subject = "Birthday Wishes from ABC..!!!"
            message = f"Hi {single_emp.name}, wishing you a very happy birthday from ABC organization...!"
            from_email = EMAIL_HOST_USER
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=[single_emp.email],
                fail_silently=True,
            )
            
        if single_emp.Date_joined.day == date.today().day and single_emp.Date_joined.month == date.today().month:
            work_years = date.today().year - single_emp.Date_joined.year
            if int(work_years) > 0:
                print(f"happy {work_years} years work anniversory:- ",single_emp)
                
                subject = "Happy Work-Anniversory Wishes from ABC..!!!"
                message = f'''Hi {single_emp.name}, 
wishing you a very happy work-anniversory from ABC organization...!
Congratulate on completing {work_years} in ABC organization...!!!'''
                from_email = EMAIL_HOST_USER
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=[single_emp.email],
                    fail_silently=True,
                )
            
    return "email send successfully...!!!"