from .production import *

DEBUG = True

ALLOWED_HOSTS.append('localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

HOST_NAME = 'http://localhost:8000'
