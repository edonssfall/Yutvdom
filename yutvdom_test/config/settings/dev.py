from .base import *

SECRET_KEY = 'django-insecure-(q2+03ru+r@q29w*f-p9b@xd52%e9ioh(a1!=+guwqxb6_7b@a'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yutvdom_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'postgres-db',
        'PORT': '5432',
    }
}