"""
Django settings for Public_Prosecution_Page project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
from django.conf.global_settings import DATABASES
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9+&nq@srw+y+y18she#y#5m(u&n-_9rnua1cubz=mr0_f_xlqw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'public-prosecution.onrender.com',
    '127.0.0.1'
]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'accounts',
    'News',
    'Reports',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Public_Prosecution_Page.urls'

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

WSGI_APPLICATION = 'Public_Prosecution_Page.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES['default'] = dj_database_url.parse('postgres://public_prosecution_page_user:x9RI8WtIVCDTxZe5xpY4cQ6GFfmnFuoM@dpg-cnl0ejvjbltc73f8iujg-a.oregon-postgres.render.com/public_prosecution_page')

#

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'publicprosecutionpage_f2hw',
        'HOST': 'dpg-cqfeo656l47c73bd6mpg-a',
        'USER': 'ahmed',
        'PASSWORD': '7cj0J2uzv7fj4zhGBhj00wFGlGBP2DO2',
        'PORT': '5432'
    }

   }


#
# DATABASES = {
#     'default': {
#
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'public_prosecution_page',
#         'HOST': 'localhost',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'PORT': ''
#     }
#
#    }
#

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ar'

LANGUAGES = [

    ('ar', _('Arabic')),
    ('en', _('English')),

    # ...
]

# COUNTRIES_ISO_ALPHA_2 = {

COUNTRIES_ISO_ALPHA_2 = {
    'ar': 'Arabic',
    'en': 'English'
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, 'locale'),
# ]

# MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# MEDIA_SERVER_URL = 'https://public-prosecution-page.onrender.com/media'
MEDIA_URL = "/media/"



# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"




LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'


# BASE_URL = 'https://public-prosecution-page.onrender.com'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
