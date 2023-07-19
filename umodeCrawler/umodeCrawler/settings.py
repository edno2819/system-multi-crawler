from pathlib import Path
from umodeCrawler.adminUI import *
from dotenv import load_dotenv
import os

SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')


load_dotenv()
config_env = os.environ

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_ROOT_ADMIN = os.path.join(BASE_DIR, "media")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)-5z+eerzt*-azz+p2=f1!vr#d5rxl+_&n5!cfs8n+3sr$k_%+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if config_env.get("DEBUG") != "false" else False

ALLOWED_HOSTS = [config_env.get("ALLOWED_HOSTS"), "localhost", "127.0.0.1", "0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    # libs
    "jazzmin",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "crawler",
    "product",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "umodeCrawler.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "umodeCrawler.wsgi.application"


# Database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": config_env.get("DB_ENGINE"),
        "NAME": config_env.get("DB_NAME"),
        "USER": config_env.get("DB_USER"),
        "PASSWORD": config_env.get("DB_PASSWORD"),
        "HOST": config_env.get("DB_HOST"),
        "PORT": config_env.get("DB_PORT"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# admin ui config jazmin
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
