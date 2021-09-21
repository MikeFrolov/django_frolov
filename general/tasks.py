import datetime

from celery import shared_task

from django.utils import timezone

from .models import Logger


@shared_task
def delete_admin_logs():
    date_to_del = timezone.now() - datetime.timedelta(days=7)
    logs_to_del = Logger.objects.filter(created__lte=date_to_del, path__contains='admin')
    logs_to_del.delete()
    return 'All of admin logs older then {} deleted'.format(date_to_del)
