"""
Django settings for nlei project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rb$efk*_1a1dpp=*nqgtjg8qlgkm_(zyk-6z=rh0r@uaod!9k%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # False for deploy

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://nlei.up.railway.app/', 'http://127.0.0.1:8000']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'lei.apps.LeiConfig',
    'frontend.apps.FrontendConfig',
    'rest_framework',
    'pwa',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nlei.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'lei/templates')],  # deixar a lista em branco por padrão
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

WSGI_APPLICATION = 'nlei.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/'

MEDIA_URL = 'images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nleigeral0@outlook.com'
EMAIL_HOST_PASSWORD = 'auascpcgjvmpfbsn'

# django summernote
INSTALLED_APPS += ('django_summernote', )


# SERVICE WORKER
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

PWA_APP_NAME = 'Núcleo de Licenciatura em engenharia Informáica'
PWA_APP_SHORT_NAME = 'NLEI'
PWA_APP_DESCRIPTION = "Núcleo formado por alunos de engenharia informática da Universidade lusiadas"
PWA_APP_THEME_COLOR = '#00C6CF'
PWA_APP_BACKGROUND_COLOR = '#3B3B3B'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
	{
		'src': 'static/imagens/icons/nlei_icon_x96.png',
		'sizes': '96x96',
        "type": "image/png"
	},
    {
        'src': 'static/imagens/icons/nlei_icon_x192.png',
        'sizes': '192x192',
        "type": "image/png"
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/imagens/icons/nlei_icon_x96.png',
        'sizes': '96x96',
        "type": "image/png"
    },
    {
        'src': 'static/imagens/icons/nlei_icon_x192.png',
        'sizes': '192x192',
        "type": "image/png"
    }
]
PWA_APP_SPLASH_SCREEN = [
	{
		'src': 'static/imagens/icons/nlei_icon_x192.png',
		'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
	}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'pt'
