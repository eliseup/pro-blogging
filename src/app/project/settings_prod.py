from project.settings import *


DEBUG = False

ALLOWED_HOSTS = ['*']  # For simplicity, but I’m aware this is not secure for production.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '96de2ef1026dc1d2c99ae1c6fb3eb313f90bce7e798d9f37b824e2eed6fc2e4f'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
    }
}


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}