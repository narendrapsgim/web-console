"""
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import base64       # for ENV_VAR decoding
import datetime     # for JWT expiration delta
import os           # for ENV_VARs and path

# General

# Set environment

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

# Main secret key use a base64 encoding to avoid possible problems with special
# characters

SECRET_KEY = base64.b64decode(
    os.environ.get('SECRET_KEY')
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# ------------------------------------------------------------------------------

# Application definition
#
# A list of strings designating all applications that are enabled in this
# Django installation.
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#installed-apps

INSTALLED_APPS = [
    # Default Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',     # Needed by Allauth
    'django.contrib.staticfiles',

    # Third party apps:
    'allauth',          # For user registration, either via email or social
    'allauth.account',  # For user registration, either via email or social
    'allauth.socialaccount',  # For user registration, either via email or social
    'crispy_forms',     # The best way to have Django DRY forms
    'captcha',          # Django reCAPTCHA form field/widget integration app.
    'reversion',        # Provides version control for model instances

    # Apps specific for console:
    'botstore',       # Bot store
    'studio',         # Bot studio
    'users',          # All user stuff
]

# The ID, as an integer, of the current site in the django_site database table.

SITE_ID = 1

# ------------------------------------------------------------------------------
#
# Middleware configuration
#
# A list of middleware to use.
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#middleware

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise will now serve your static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------------------------
#
# Authentication configuration
#
# All settings played to user authentication and authorization

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Apart of standard Django Hasher we use a custom wrapper to migrate old users
# passwords. After first login users password is updated to standard Django
# PBKDF2 SHA256.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'users.hashers.PBKDF2WrappedSHA256PasswordHasher',
]

# Legacy constant Salt
LEGACY_SALT = base64.b64decode(
    os.environ.get('LEGACY_SALT')
).decode('utf-8')

LOGIN_REDIRECT_URL = '/home/'

# Allow loging using emails only (kind of industrial standard)
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Determines whether or not an e-mail address is automatically confirmed by a
# GET request. GET is not designed to modify the server state, though it is
# commonly used for email confirmation. To avoid requiring user interaction,
# consider using POST via Javascript in your email confirmation template as an
# alternative to setting this to True.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True ??

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# User is blocked from logging in until the email address is verified.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 16
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# Retyping passwords is annoying!
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# A string pointing to a custom form class that is used during signup to ask
# the user for additional input.
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

# Usernames are setup by application, longer are always harder to guess
ACCOUNT_USERNAME_MIN_LENGTH = 8

# Default redirect after user is loged in
LOGIN_REDIRECT_URL = '/'

# JSON web token
# Used to connect to the API

# This is the secret key used to sign the JWT. Make sure this is safe and not
# shared or public.
JWT_SECRET_KEY = base64.b64decode(
    os.environ.get('JWT_SECRET_KEY')
)

# Algorithm for cryptographic signing in PyJWT
JWT_ALGORITHM = 'HS256'

# This is an instance of Python's `datetime.timedelta`. This will be added to
# datetime.utcnow() to set the expiration time.
JWT_EXPIRATION_DELTA = datetime.timedelta(days=60)


# ReCaptcha

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

NOCAPTCHA = True

# ------------------------------------------------------------------------------
#
# Sessions
#
# Settings for `django.contrib.sessions  sessions are stored in Redis
#
# https://docs.djangoproject.com/en/1.11/ref/settings/#sessions
# http://niwinz.github.io/django-redis/latest/#_configure_as_session_backend

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# We’re using cache-based session storage, this selects the cache to use.
SESSION_CACHE_ALIAS = 'sessions'

# Since it’s trivial for a packet sniffer (e.g. Firesheep) to hijack a user’s
# session if the session cookie is sent unencrypted, there’s really no good
# excuse to leave this off. It will prevent you from using sessions on insecure
# requests and that’s a good thing.
# SESSION_COOKIE_SECURE = True

# ------------------------------------------------------------------------------
#
# Routing configuration
#
# A string representing the full Python import path to your root URLconf
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#root-urlconf

ROOT_URLCONF = 'app.urls'

# ------------------------------------------------------------------------------
#
# Templates
#
# A list containing the settings for all template engines to be used
# with Django.
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'botstore', 'templates'),
            os.path.join(BASE_DIR, 'studio', 'templates'),
            os.path.join(BASE_DIR, 'users', 'templates'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------------------------------------------------------
#
# Form template
#
# Twitter Bootstrap version 3.
#
# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# ------------------------------------------------------------------------------
#
# WebServer configuration
#
# The full Python path of the WSGI application object that Django’s built-in
# servers (e.g. runserver) will use.
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#wsgi-application

WSGI_APPLICATION = 'app.wsgi.application'

# ------------------------------------------------------------------------------
#
# Database
#
# A dictionary containing the settings for all databases to be used
# with Django.
#
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME', 'console_db'),
        'USER': os.environ.get('DATABASE_USER', 'console_app'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', '12345678'),
        'HOST': os.environ.get('DATABASE_HOST', 'mysql'),
        'PORT': os.environ.get('DATABASE_PORT', '3306'),
        'ATOMIC_REQUESTS': True,
    },
}

# ------------------------------------------------------------------------------
#
# Cache configuration
#
# A dictionary containing the settings for all caches to be used with Django.
#
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-CACHES
# http://niwinz.github.io/django-redis/latest/#_configure_as_cache_backend

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://:%s@%s:%s/1' % (
                os.getenv('CACHE_SERVICE_PASSWORD'),
                os.getenv('CACHE_SERVICE_HOST', 'redis'),
                os.getenv('CACHE_SERVICE_PORT', 6379)
            ),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
    'sessions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://:%s@%s:%s/2' % (
                os.getenv('CACHE_SERVICE_PASSWORD'),
                os.getenv('CACHE_SERVICE_HOST', 'redis'),
                os.getenv('CACHE_SERVICE_PORT', 6379)
            ),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}


# Don't cache templates for development
TEMPLATES_CACHE_AGE = 0

# ------------------------------------------------------------------------------
#
# Internationalization
#
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# Default language code
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Where to search for translation strings
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'botstore', 'locale'),
    os.path.join(BASE_DIR, 'studio', 'locale'),
    os.path.join(BASE_DIR, 'users', 'locale'),
    os.path.join(BASE_DIR, 'locale'),
]

# Languages we are using
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'France'),
    ('pl', 'Polski'),
]

# ------------------------------------------------------------------------------
#
# Static files (CSS, JavaScript, Images)
#
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')

STATIC_URL = STATIC_HOST + '/static/'

# In addition to using a `static/` directory inside your apps, define a list of
# directories where Django will also look for static files that aren’t tied to
# a particular app
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# WhiteNoise comes with a storage back-end which automatically takes care of
# compressing your files and creating unique names for each version so they can
# safely be cached forever.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media
#
# User generated content
MEDIA_URL = base64.b64decode(
    os.environ.get('MEDIA_URL')
).decode('utf-8')

# ------------------------------------------------------------------------------
#
# API connection
#
# APIs url is different in each environment, timeout error would be thrown
# after 1s
#

API_URL = os.environ.get('API_URL')
API_TIMEOUT = 1

# ------------------------------------------------------------------------------
#
# Environments specific settings

if ENVIRONMENT == 'development':
    """
    Development settings

    - Run in Debug mode

    - Use local MySQL as database
    - Use Mailhog proxy for outgoing emails

    - Add Django Debug Toolbar
    """

    import socket   # used by django-debug-toolbar

    DEBUG = os.environ.get('DEBUG', True)

    TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

    # Allow all hosts in development mode
    ALLOWED_HOSTS = ['*']

    EMAIL_PORT = 1025
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'mailhog')

    # --------------------------------------------------------------------------
    #
    # Logging
    #
    # Logs would be colored using `coloredlogs`

    DJANGO_LOG_LEVEL = 'INFO'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'colored': {
                '()': 'coloredlogs.ColoredFormatter',
                'format': '%(name)s.%(funcName)2s - %(message)s %(filename)s:%(lineno)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', DJANGO_LOG_LEVEL),
            },
            'botstore': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', DJANGO_LOG_LEVEL),
            },
            'studio': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', DJANGO_LOG_LEVEL),
            },
            'users': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', DJANGO_LOG_LEVEL),
            }
        },
    }

    # --------------------------------------------------------------------------
    #
    # django-debug-toolbar

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
        '0.0.0.0'
    ]

    # Docker in VM hack

    ip = socket.gethostbyname(
        socket.gethostname()
    )

    INTERNAL_IPS += [
        ip[:-1] + '1'
    ]

    # End of hack

elif ENVIRONMENT == 'test':
    """
    Test settings

    - Use SQLite as database
    """

    # Debug
    #
    # Turn debug off so tests run faster

    DEBUG = False
    TEMPLATES[0]['OPTIONS']['debug'] = False

    # --------------------------------------------------------------------------
    #
    # Databases
    #
    # Use a faster storage system

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'simple_test_db'
        }
    }

    # Mail settings
    #
    # --------------------------------------------------------------------------

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025

    # In-memory email backend stores messages in django.core.mail.outbox
    # for unit testing purposes
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

    # --------------------------------------------------------------------------
    #
    # Testing

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    # --------------------------------------------------------------------------
    #
    # Password hashing
    #
    # Use fast password hasher so tests run faster

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    # --------------------------------------------------------------------------
    #
    # Template loaders
    #
    # Keep templates in memory so tests run faster

    TEMPLATES[0]['APP_DIRS'] = False
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]

elif ENVIRONMENT == 'production':

    """
    Production settings

    - Enable stronger password
    - Use SendGrid for mailing
    - Setup secure Allowed hosts
    - Enable Secure session cookie
    """

    #
    # Security
    #

    # A list of strings representing the host/domain names that this Django
    # site can serve. This is a security measure to prevent HTTP Host header
    # attacks, which are possible even under many seemingly-safe web server
    # configurations.
    ALLOWED_HOSTS = [
        'console.hutoma.ai',
        'development-console.hutoma.ai'
    ]

    # Whether to use a secure cookie for the session cookie. If this is set to
    # True, the cookie will be marked as “secure,” which means browsers may
    # ensure that the cookie is only sent under an HTTPS connection.
    SESSION_COOKIE_SECURE = True

    # Password validation
    #
    # The list of validators that are used to check the strength of
    # user’s passwords.
    #
    # See: https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

    # --------------------------------------------------------------------------
    #
    # Logging
    #

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', 'INFO'),
            },
            'users': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', 'INFO'),
            },
            'studio': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', 'INFO'),
            },
            'botstore': {
                'handlers': ['console'],
                'level': os.environ.get('LOG_LEVEL', 'INFO'),
            },
        },
    }

    # --------------------------------------------------------------------------
    #
    # Emails
    #
    # TODO: move to SendGrid
    #

    INSTALLED_APPS += ['anymail']

    ANYMAIL = {
        'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': 'mg.samp.la',
    }

    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    DEFAULT_FROM_EMAIL = 'no-reply@mg.samp.la'
    EMAIL_SUBJECT_PREFIX = '🤖 from Hu:toma: '

    # --------------------------------------------------------------------------
    #
    # Cache
    #

    # Default cache for Templates set to 15 minutes
    TEMPLATES_CACHE_AGE = 60 * 15

    # --------------------------------------------------------------------------
