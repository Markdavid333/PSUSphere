"""
Django settings for projectsite project.
"""

from pathlib import Path
import os
import socket

# Base directory (points to the outer projectsite folder)
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = 'django-insecure-tt3_v-=*t&8l3+msi0qf2!hp0c1_&-!0zmyy#n&ioji!$*el-s'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'markdavid33.pythonanywhere.com']


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    'studentorg',
    'widget_tweaks',
]

if "pythonanywhere" in socket.gethostname():
    SITE_ID = 2  # production site (psusphere.pythonanywhere.com)
else:
    SITE_ID = 1  # local site (127.0.0.1:8000)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'projectsite.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'projectsite.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/' # where @login_required will send users
LOGIN_REDIRECT_URL = '/' # where to go after successful login
LOGOUT_REDIRECT_URL = '/accounts/login/' # after logout, go back to login
ACCOUNT_LOGOUT_REDIRECT_URL = '/' # where to redirect after logout
ACCOUNT_LOGOUT_ON_GET = True # logout immediately on GET
ACCOUNT_LOGIN_METHODS = {"username", "email"} # allow login with username OR email
ACCOUNT_SIGNUP_FIELDS = [
"username*",
"email*",
"password1*",
"password2*",
]


# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===============================
# STATIC FILES (FIXED SECTION)
# ===============================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)