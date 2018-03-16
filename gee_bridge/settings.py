"""
Django settings for gee_bridge project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import datetime
import os

import ee
from firebase_admin import credentials

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'
# STATIC_URL = 'https://storage.googleapis.com/gee_bridge/static/'

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
    'django.contrib.sites',
    'django_extensions',
    'polymorphic',
    'helloworld',
    'storages',
    'corsheaders',
    'bootstrap4',
    # rest
    'rest_framework',
    'drf_yasg',
    'rest_framework_swagger',
    'rest_framework_docs',
    # rest security
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'rest_auth_firebase',
    'djoser',
    'drfpasswordless',
    # oauth2
    'oauth2_provider',
    # custom
    'gee_bridge',
    'api',
    'httpproxy',
    'gee_agent',
    'channels',
    'mapclient',
    'webpack_loader',
    'webmapping'
]

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gee_bridge.urls'

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

WSGI_APPLICATION = 'gee_bridge.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_yaml.parsers.YAMLParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_auth_firebase.authentication.FirebaseAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework_jwt.authentication.TokenAuthentication',
        # oauth2
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000000),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'JSON_EDITOR': True,
    'LOGIN_URL': '/admin/login',
    'LOGOUT_URL': '/admin/logout'
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# JSONField
# USE_NATIVE_JSONFIELD = True

# Email configuration
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

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

# Api registration and password management
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
}

# Passwordless configuration
PASSWORDLESS_AUTH = {
    # Allowed auth types, can be EMAIL, MOBILE, or both.
    'PASSWORDLESS_AUTH_TYPES': ['EMAIL'],
    # Amount of time that tokens last, in seconds
    'PASSWORDLESS_TOKEN_EXPIRE_TIME': 15 * 60,

    # The user's email field name
    'PASSWORDLESS_USER_EMAIL_FIELD_NAME': 'email',

    # The user's mobile field name
    'PASSWORDLESS_USER_MOBILE_FIELD_NAME': 'mobile',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if email is changed.
    'PASSWORDLESS_USER_MARK_EMAIL_VERIFIED': False,
    'PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME': 'email_verified',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if mobile number is changed.
    'PASSWORDLESS_USER_MARK_MOBILE_VERIFIED': False,
    'PASSWORDLESS_USER_MOBILE_VERIFIED_FIELD_NAME': 'mobile_verified',

    # The email the callback token is sent from
    'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': None,

    # The email subject
    'PASSWORDLESS_EMAIL_SUBJECT': "Your Login Token",

    # A plaintext email message overridden by the html message.
    # Takes one string.
    'PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE': "Enter this token to sign in: %s",

    # The email template name.
    'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME':
        "passwordless_default_token_email.html",

    # The SMS sent to mobile users logging in. Takes one string.
    'PASSWORDLESS_MOBILE_MESSAGE': "Use this code to log in: %s",

    # Registers previously unseen aliases as new users.
    'PASSWORDLESS_REGISTER_NEW_USERS': True,

    # Suppresses actual SMS for testing
    'PASSWORDLESS_TEST_SUPPRESSION': False
}

# CORS management
CORS_ORIGIN_ALLOW_ALL = True

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# Extra places for collectstatic to find static files.

# STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Shapefile directory for Gaul
SHAPEFILE_DIR = os.path.join(PROJECT_ROOT, 'gaul')

#
# Google Drive Storage Settings
#
# Path to the json file key
GOOGLE_JSON_KEY_DIR = os.path.join(BASE_DIR, "google")
# GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(
#     GOOGLE_JSON_KEY_DIR, 'WaterProductivity-a15018b72eec.json')

# Google Cloud Storage
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'fao-wapor-bucket'
GS_PROJECT_ID = '1009145000126'
# Don't use GS_CREDENTIALS
# see issue https://github.com/jschneier/django-storages/issues/455
GOOGLE_APPLICATION_CREDENTIALS = os.path.join(
    GOOGLE_JSON_KEY_DIR, 'WaterProductivity-a15018b72eec.json'
)
GOOGLE_CLOUD_STORAGE_UPLOAD_FOLDER = 'geebridge'

# To be removed since the development database is complaining about this
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = GOOGLE_APPLICATION_CREDENTIALS

# Google Earth Engine Settings
#
# GEE hostname
GEE_PUBLIC_BASE_URL = 'https://earthengine.googleapis.com/'
GEE_MAP_TILES_PATTERN = '/map/z/x/y?token='
#
# GEE authentication
# The service account email address authorized by your Google contact.
EE_ACCOUNT = 'fao-wapor@fao-wapor.iam.gserviceaccount.com'
# The private key associated with your service account in Privacy Enhanced
# Email format (deprecated version .pem suffix, new version .json suffix).
EE_PRIVATE_KEY_FILE = os.path.join(
    GOOGLE_JSON_KEY_DIR, 'WaterProductivity-a15018b72eec.json')
# Service account scope for GEE
GOOGLE_SERVICE_ACCOUNT_SCOPES = [
    'https://www.googleapis.com/auth/fusiontables',
    'https://www.googleapis.com/auth/earthengine'
]
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT,
                                              EE_PRIVATE_KEY_FILE,
                                              GOOGLE_SERVICE_ACCOUNT_SCOPES)

# Firebase settings
FIREBASE_ACCOUNT = 'firebase-adminsdk-6s5ce@spring-firebase-demo.iam.gserviceaccount.com' # EE_ACCOUNT
FIREBASE_PRIVATE_KEY_FILE = os.path.join(
    GOOGLE_JSON_KEY_DIR, 'spring-firebase-demo-firebase-adminsdk-6s5ce-68de378780.json')
FIREBASE_SERVICE_ACCOUNT_SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/firebase',
    'https://www.googleapis.com/auth/firebase.readonly'
]
FIREBASE_CREDENTIALS = credentials.Certificate(FIREBASE_PRIVATE_KEY_FILE)

# Proxy GEE tiles server
PROXY_BASE_URL = 'https://earthengine.googleapis.com/map'  # GEE_PUBLIC_BASE_URL
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
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'asgi_redis.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('localhost', 6379)],
#         },
#         'ROUTING': 'webmapping.routing.channel_routing',
#     },
# }

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
        # '/static/bundles/',  # end with slash
        'BUNDLE_DIR_NAME': os.path.join('bundles/'),
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json')
    }
}
