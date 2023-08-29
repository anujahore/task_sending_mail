from celery import shared_task
# from django.conf import settings
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django_celery_t.settings import EMAIL_HOST_USER


@shared_task(bind=True)
def send_mail_task(self):
    print("sending mail ---- task ---------")
    users = User.objects.all()
    for i in users:
        mail_subject = "testing mail for celery "
        message = "hi there.. this mail is for testing celery if working or not...!"
        send_to = i.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[send_to],
            fail_silently=True,
            
        )
    return "Done sending mail"
    



@shared_task(bind=True)
def demo_task(self):
    # operations
    for i in range(10):
        print(i)
    return "done"

# =======================================================

# from mainapp.models import TestingEmp
# from datetime import date

# def emp_birthday(request):
#     all_emps = TestingEmp.objects.all()
#     for single_emp in all_emps:
#         if single_emp.birthdate.day == date.today().day and single_emp.birthdate.month == date.today().month:
#             print(single_emp)
#         if single_emp.Date_joined.day == date.today().day and single_emp.Date_joined.month == date.today().month:
#             print(single_emp)
        
#     return Http



