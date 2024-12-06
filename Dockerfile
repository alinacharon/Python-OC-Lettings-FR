FROM python:3.8-slim


ARG SENTRY_DSN

ENV SENTRY_DSN=${SENTRY_DSN}

ARG SECRET_KEY_DJANGO

ENV SECRET_KEY_DJANGO=${SECRET_KEY_DJANGO}

WORKDIR /app

COPY . .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate --noinput

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]