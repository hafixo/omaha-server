# coding: utf8

from .settings import *

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=omaha_server,omaha',
    '--cover-inclusive',
    '--with-doctest',
]

# Tricks to speed up Django tests

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}
SOUTH_TESTS_MIGRATE = False
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'memory'

CACHES['default'] = {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
}

CACHES['statistics'] = {
    'BACKEND': 'redis_cache.cache.RedisCache',
    'LOCATION': '{REDIS_HOST}:{REDIS_PORT}:{REDIS_DB}'.format(
        REDIS_PORT=os.environ.get('REDIS_STAT_PORT', REDIS_PORT),
        REDIS_HOST=os.environ.get('REDIS_STAT_HOST', REDIS_HOST),
        REDIS_DB=os.environ.get('REDIS_STAT_DB', 13)),
    'OPTIONS': {
        'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
    }
}


OMAHA_UID_KEY_PREFIX = 'test:uid'