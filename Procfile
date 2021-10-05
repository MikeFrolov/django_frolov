web: gunicorn django_frolov.wsgi:application --log-file - --log-level debug
worker: celery -A django_frolov worker --beat -S django --l info
python manage.py collectstatic --noinput
manage.py migrate