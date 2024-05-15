import os
import environ
from .base import *

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Secret Key
SECRET_KEY = env("SECRET_KEY")

# Debug
DEBUG = env.bool("DEBUG", default=False)

# Allowed Hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])

# Email Backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}

# Installed Apps
INSTALLED_APPS += ["django_extensions"]

