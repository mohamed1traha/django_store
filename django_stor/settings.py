"""
Django settings for django_stor project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_*%nop=w)1qxs!fif&sxq()3swh)$$pj1bxq_2tzg$092-fbsh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stor',
    'checkout',
    'reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_stor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'stor.custom.stor_website',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_stor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_stor',
        'USER' : 'postgres',
        'PASSWORD': 'MOHAMED', 
        'HOST': 'localhost', 
        'PORT' : '',

    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ar-as'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Looking to send emails in production? Check out our Email API/SMTP product!





# Looking to send emails in production? Check out our Email API/SMTP product!
# Looking to send emails in production? Check out our Email API/SMTP product!

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '4671076bec2f3a'
EMAIL_HOST_PASSWORD = '4b23e2ac36cf31'
EMAIL_PORT = '2525'



SITE_URL ='http://127.0.0.1:8000/'



STRIPE_PUBLISHABLE_KEY="pk_test_51QmAz803AZn20b37mrSv8eRWcIipTmZbFTO8Ix32pexMTQJ5QQsqLLpYh8IxO2peZBfptcXb0gH6urFxeDnUuUeq00eOevatip"

STRIPE_SECRET_KEY="sk_test_51QmAz803AZn20b37gIsun0jagiNKNeeZWWVipxzdh9L2QQr0zOFQHJ5rccKnIJ3uefR22z2qubnb2N279tMxqnql00kPJb8Oqj"

CURRENCY= 'USD'


STRIPE_WEBHOOK_SECRET = 'whsec_096d7f61391214ac1ec672392adc0d146488d836fa58a3e7e14e24d9d34c87b5'
APPEND_SLASH = False