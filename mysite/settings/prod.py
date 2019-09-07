from .common import *

DEBUG = True
ALLOWED_HOSTS = ['eatoutpay.pythonanywhere.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'ordermandb.sqlite3'),
    }
}


AWS_ACCESS_KEY_ID = 'AKIAVNC3EVGMGNL5BLSR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'eatoutpay'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION_STATIC = 'static'
AWS_LOCATION_MEDIA = 'media'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mysite/static'),
]

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION_STATIC)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION_MEDIA)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'