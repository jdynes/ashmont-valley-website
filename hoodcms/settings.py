"""
Django settings for hoodcms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

CMS_PERMISSION = True
CMS_TEMPLATES = (
    ('cms/normal.html', 'Normal Page'),
)

DATE_FORMAT = 'm/d/Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'm/d/Y H:i'

ROOT_URLCONF = 'hoodcms.urls'

WSGI_APPLICATION = 'hoodcms.wsgi.application'

SITE_ID = 1
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#
# --- Above this line, settings can be over-ridden for deployment
# 
from hoodcms import *

# Restrict to a specific address
SITE_ROOT = "http://%s" % SITE_ADDRESS
ALLOWED_HOSTS = [SITE_ADDRESS]

INSTALLED_APPS = (
    'hoodcms',

    'mptt', 
    'menus',
    'sekizai',

    'djangocms_picture',
    'djangocms_link',
    'djangocms_text_ckeditor',
    'cms',

    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

# Make django-cms 3.0.12 compatible with django-1.7.x
MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
    # This is nuts
    'djangocms_picture' : 'djangocms_picture.migrations_django',
    'djangocms_link' : 'djangocms_link.migrations_django',
    'djangocms_text_ckeditor' : 'djangocms_text_ckeditor.migrations_django',
}

# Place where static files are served in live (not used in dev)
STATIC_ROOT = os.path.join(DATA_PATH, 'static')
STATIC_URL = '/static/'

# Place where files can be uploaded, served in live and dev
MEDIA_ROOT = os.path.join(DATA_PATH, 'media')
MEDIA_URL = '/media/'

