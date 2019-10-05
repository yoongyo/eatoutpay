from .common import *

DEBUG = False
ALLOWED_HOSTS = ['eatoutpay.pythonanywhere.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'ordermandb.sqlite3'),
    }
}

with open('secret.json', 'r') as f:
    secret = json.loads(f.read())


def get_secret(setting, secret=secret):
    try:
        return secret[setting]
    except:
        msg = "Set key '{0}' in secret.json".format(setting)


AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
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