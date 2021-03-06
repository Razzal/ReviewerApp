"""
Django settings for class_review_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*yp-z#25sm@*z!tlyg-o_)j09$q!qn2^exdt0#y&=zc5vt)hiw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.amazingunicorn.com',
    'www.amazingunicorn.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'axes',
    'movie_reviewer'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'class_review_app.urls'

WSGI_APPLICATION = 'class_review_app.wsgi.application'

LOGIN_REDIRECT_URL = "/reviewer/profile"
LOGIN_URL = "/reviewer/login"
LOGOUT_URL = "/reviewer/logout"
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

#Session behavior settings
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/razzal/webapps/moviereviewer_static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "movie_reviewer/static/"),
)
if TEMPLATE_DEBUG == True:
    MEDIA_URL= "F:/class_review_app/movie_reviewer/images/"
    MEDIA_ROOT= "F:/class_review_app/movie_reviewer/images/"


TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth', 'django.core.context_processors.debug', 'django.core.context_processors.i18n', 'django.core.context_processors.media', 'django.core.context_processors.static', 'django.core.context_processors.tz', 'django.contrib.messages.context_processors.messages', 'django.core.context_processors.request' )

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader')

# Axes authentication lockout setup
AXES_LOGIN_FAILURE_LIMIT = 3
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = 12
AXES_LOCKOUT_TEMPLATE = os.path.join(BASE_DIR,'movie_reviewer/templates/reviewer/lockout.html')
AXES_LOCKOUT_URL = '/reviewer/lockout'
AXES_USERNAME_FORM_FIELD = 'user_name'

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'class_movie_app_db',
        'USER': 'application',
    }
}
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'class_movie_app_db',
        'USER': 'application',
        'PASSWORD': 'apppass',
        'HOST': 'web440.webfaction.com',
        'PORT': '5432',
    }
}