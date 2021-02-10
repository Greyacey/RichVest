web: gunicorn manage:app --bind 0.0.0.0:$PORT --timeout 120 --log-level=info -k gevent -w 1
release: python manage.py db upgrade && python manage.py seed_admin