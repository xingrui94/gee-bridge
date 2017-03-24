"""
Django settings for mycustomdjango project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import datetime
import ee

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'
# STATIC_URL = 'http://storage.googleapis.com/mycustomdjango/static/'

# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#gy*!m7zd^(ln*pm(&a&)di1whp9%968+skr_20q1p0$intee='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polymorphic',
    'helloworld',
    'gdstorage',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'api',
    'httpproxy',
    'gee_agent',
    'mapclient',
    'channels',
    'webpack_loader'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mycustomdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mycustomdjango.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000000),
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Shapefile directory for Gaul
SHAPEFILE_DIR = os.path.join(PROJECT_ROOT, 'gaul')

#
# Google Drive Storage Settings
#
# Path to the json file key
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = 'MyCustomDjango-dbd004fbce00.json'

#
# Google Earth Engine Settings
#
# GEE hostname
GEE_PUBLIC_BASE_URL = 'https://earthengine.googleapis.com/'
GEE_MAP_TILES_PATTERN = '/map/z/x/y?token='
#
# GEE authentication
# The service account email address authorized by your Google contact.
EE_ACCOUNT = 'mycustomdjango@appspot.gserviceaccount.com'
# The private key associated with your service account in Privacy Enhanced
# Email format (deprecated version .pem suffix, new version .json suffix).
EE_PRIVATE_KEY_FILE = 'MyCustomDjango-dbd004fbce00.json'
# Service account scope for GEE
GOOGLE_SERVICE_ACCOUNT_SCOPES = ['https://www.googleapis.com/auth/fusiontables',
                                 'https://www.googleapis.com/auth/earthengine']
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT,
                                              EE_PRIVATE_KEY_FILE,
                                              GOOGLE_SERVICE_ACCOUNT_SCOPES)

# Proxy GEE tiles server
PROXY_BASE_URL = 'https://earthengine.googleapis.com/map' # GEE_PUBLIC_BASE_URL
PROXY_LOCATION = '/maps/'

# Base url
BASE_URL = 'http://localhost:8000'

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgiref.inmemory.ChannelLayer',
        'ROUTING': 'mapclient.routing.channel_routing',
    },
}

# Standard login
LOGIN_REDIRECT_URL = '/webmap/'
LOGIN_URL = '/login/'

# Mapclient
MAP_TYPES = (
    ('TMS', 'tms'),
)

# React
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': os.path.join('bundles/'),  # '/static/bundles/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json')
    }
}
