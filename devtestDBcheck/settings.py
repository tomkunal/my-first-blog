"""
Django settings for devtestDBcheck project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*h1+uhw&$b$0lb5r9=ivc_24klf8-9=f35y#9&64)&ti1)ug-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['hqnvwbtd01','localhost','hlahoti-lt1', '127.0.0.1','kunaltom.pythonanywhere.com']

# DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap.html'
# Application definition

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'WARNING',
#     },
# }
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
INSTALLED_APPS = [
    'GetData.apps.GetdataConfig',
    #'GetData.Game.GetdataConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django_filters',
   # 'django.contrib.staticfiles',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'devtestDBcheck.urls'

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# Find templates in the same folder as settings.py.
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',"os.path.join(SETTINGS_PATH, 'templates')"],
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

WSGI_APPLICATION = 'devtestDBcheck.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  'db.sqlite3',
    }
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
"""
DATABASES = {
   'default': {
        'NAME':'DevtestDB2',
        'ENGINE':'sql_server.pyodbc',
        'HOST':'HQNVSQL171',
        'USER':'DevTest_User',
        'PASSWORD':'Nvidia@2o1o',
        'OPTIONS': {
            'driver':'ODBC Driver 13 for SQL Server',
            #'MARS_Connection': True,
            
        },
    },
    'spider_db': {
        'NAME': 'Experi1',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'RNNVSQL174',
        'USER': 'wbt_user',
        'PASSWORD': 'wbt_user@123',
        'OPTIONS': {
            # 'driver': 'ODBC Driver 11 for SQL Server',
            'driver': 'ODBC Driver 13 for SQL Server',
            #'MARS_Connection': True,
            'host_is_server': True,
        },
    }
   # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}

"""
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_URL = '/static/'

##STATICFILES_DIRS = [
##   os.path.join(BASE_DIR, "static"),
##]
