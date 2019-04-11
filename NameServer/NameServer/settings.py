import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jtujou)&(owyw9%b@1595w$f$zx4eb#t8qd)p65$jfn-ucr0aa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set this variable when the ns is not served at the root of the provided address
NGINX_PRE = os.environ.get('NAMESERVER_NGINX_PRE', '')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'rest_framework',
    'rest_framework.authtoken',

    # 'rest_framework_swagger',

    # 'rest_auth',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'rest_auth.registration',

    # 'rest_framework_docs',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    # 'DEFAULT_PERMISSION_CLASSES': [
    #   'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_xml.parsers.XMLParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer'
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NameServer.urls'

APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'NameServer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('NAMESERVER_DB_PATH', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []
#    [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
# ]

# SWAGGER_SETTINGS = {
# 'LOGIN_URL': 'NameServer:login',
# 'LOGOUT_URL': 'NameServer:logout',
#    'USE_SESSION_AUTH': False,
#    'DOC_EXPANSION': 'list',
#    'APIS_SORTER': 'alpha',
#    'SECURITY_DEFINITIONS': None,
# }


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# REST_AUTH_REGISTER_SERIALIZERS = {
#    'REGISTER_SERIALIZER': 'api.serializers.InstanceSerializer'
# }

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# CUSTOM USER MODEL
AUTH_USER_MODEL = 'api.Instance'
STATIC_URL = '/'+NGINX_PRE+'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

SITE_ID = 1

# CUSTOM USER MODEL
AUTH_USER_MODEL = 'api.Instance'