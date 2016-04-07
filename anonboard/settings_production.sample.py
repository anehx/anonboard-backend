import * from settings

DEBUG = False

STATIC_ROOT = '/var/www/anonboard/django-static/'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'anonboard',
        'USER':     'anonboard',
        'PASSWORD': '*********',
        'HOST':     'localhost'
    }
}
