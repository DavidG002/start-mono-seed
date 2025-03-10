FROM python:3.10
WORKDIR /app
COPY apps/backend/django/pyproject.toml ./
RUN pip install poetry && poetry install --no-root
COPY apps/backend/django/ .
RUN mkdir -p /app/db
RUN poetry run python manage.py migrate
RUN poetry run python manage.py collectstatic --noinput
RUN poetry run python manage.py shell < create_superuser.py
EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]