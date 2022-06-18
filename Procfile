web: gunicorn gettingstarted.wsgi
web: gunicorn hospital.py:best_hospital
web: gunicorn hospital.py:hospital:best_hospital --preload
web: python hospital.py runserver
web: gunicorn --pythonpath path_wsgi_application --log-file -
