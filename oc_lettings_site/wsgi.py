import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

secret_key = os.getenv('SECRET_KEY_DJANGO')
if not secret_key:
    raise ValueError("The SECRET_KEY_DJANGO environment variable is not set.")

os.environ['SECRET_KEY'] = secret_key

application = get_wsgi_application()