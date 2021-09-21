from celery import shared_task

from django.core.mail import send_mail


@shared_task
def contact_us_form(title, message, email_from, email_to):
    email = send_mail(title, message, email_from, email_to, fail_silently=False)

    if email:
        return 'Success: Sent email from {}!'.format(email_from)
    else:
        return 'Email sending error!'
