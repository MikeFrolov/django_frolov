web: gunicorn django_frolov.wsgi:application --log-file - --log-level debug
worker: celery -A django_frolov worker -events -loglevel info
beat: celery -A django_frolov beat
python manage.py collectstatic --noinput
manage.py migrate