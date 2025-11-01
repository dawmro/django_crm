# django_crm
[WIP] Customer Relationship Manager created using Python, Django, Google Auth Platform, Tiger Data, TimescaleDB, and more.


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
