release: python manage.py migrate
web: gunicorn Public_Prosecution_Page.wsgi --log-file -

release: python manage.py collectstatic --no-input
