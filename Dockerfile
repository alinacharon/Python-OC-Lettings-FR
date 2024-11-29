FROM python:3.8-slim

WORKDIR /app

# Копируем все файлы в контейнер
COPY . .

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Выполняем миграции
RUN python manage.py migrate --noinput

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--worker-class", "gevent"]