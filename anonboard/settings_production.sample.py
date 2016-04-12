from settings import *

DEBUG = False

STATIC_ROOT = '/var/www/anonboard/django-static/static'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'anonboard',
        'USER':     'anonboard',
        'PASSWORD': '*********',
        'HOST':     'localhost'
    }
}
