from .base import *
import dj_database_url
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        **dj_database_url.parse(config('DATABASE_URL')),
        'ENGINE': 'django.db.backends.postgresql',
    }
}