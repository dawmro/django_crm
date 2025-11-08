# django_crm
[WIP] Customer Relationship Manager created using Python, Django, Google Auth Platform, Tiger Data, TimescaleDB, and more.

## Notes
uv python install 3.14
uv init --python 3.14
uv add "Django>=5.2,<6.0"
.\.venv\Scripts\activate
uv add pip --dev
uv sync
cd src
uv run django-admin startproject dchome .
cd ../
uv export --no-dev --no-hashes -o requirements.txt
uv add pre-commit
uv run pre-commit install
uv add "django-googler"
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py startapp contacts
python manage.py makemigrations
python manage.py migrate
uv add python-dotenv
python manage.py collectstatic
https://docs.djangoproject.com/en/5.2/howto/static-files/
python manage.py collectstatic --no-input
https://whitenoise.readthedocs.io/en/stable/django.html
uv add rav --dev
rav download staticfiles_dev
https://flowbite.com/
uv add "psycopg[binary]"
uv add dj-database-url
uv add django-timescaledb
Stuck at "Your service is being deployed!"
