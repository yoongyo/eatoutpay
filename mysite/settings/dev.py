from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
  os.path.join(BASE_DIR,  'mysite', 'static'),
]
