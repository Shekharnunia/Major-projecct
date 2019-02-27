"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from decouple import config
import dj_database_url

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'bootstrap_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # local
    # 'main',
    'polls',
    'blog',
    # 'account',
    'users',
    'Newsletter',
    'control_panel',
    'qa',
    'assignment',
    'search',
    'comments',

    # third party
    'widget_tweaks',
    'crispy_forms',
    'sorl.thumbnail',
    "taggit",
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'tellme',

    'pagedown',
    'contact_form',
    'django_extensions',
    'storages',
]

TELLME_FEEDBACK_EMAIL = 'shekharnunia@gmail.com'

ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

TAGGIT_CASE_INSENSITIVE = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

INTERNAL_IPS = '127.0.0.1'

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.media',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'myproject.wsgi.application'

AUTH_USER_MODEL = 'users.User'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'puzzles',
        'USER': 'root',
        'PASSWORD': 'shekhar@6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# '/var/www/static'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'settings', 'news', 'about', 'help',
                              'signin', 'signup', 'signout', 'terms', 'privacy',
                              'cookie', 'new', 'login', 'logout', 'administrator',
                              'join', 'account', 'username', 'root', 'blog',
                              'user', 'users', 'billing', 'subscribe', 'reviews',
                              'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                              'home', 'job', 'jobs', 'contribute', 'newsletter',
                              'shop', 'profile', 'register', 'auth',
                              'authentication', 'campaign', 'config', 'delete',
                              'remove', 'forum', 'forums', 'download',
                              'downloads', 'contact', 'blogs', 'feed', 'feeds',
                              'faq', 'intranet', 'log', 'registration', 'search',
                              'explore', 'rss', 'support', 'status', 'static',
                              'media', 'setting', 'css', 'js', 'follow',
                              'activity', 'questions', 'articles', 'network', ]


LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'qa:index_noans'
LOGOUT_REDIRECT_URL = 'account_login'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')
MANAGERS = [('Shekhar', 'shekharnunia@gmail.com'), ('Shekhar', 'shekharnunia1992@gmail.com')]
ADMINS = ('Shekhar', 'shekharnunia@gmail.com')
EMAIL_SUBJECT_PREFIX = '[Puzzles]'
