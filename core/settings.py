from pathlib import Path
from decouple import Config, RepositoryEnv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

config = Config(RepositoryEnv('/app/.env'))

# Security settings
SECRET_KEY = config("DJANGO_SECRET")
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="localhost").split(",")

# Installed apps
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "rest_framework",
    "payments.apps.PaymentsConfig",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

# Root URL configuration
ROOT_URLCONF = "core.urls"

# Database (SQLite for development; replace with PostgreSQL in production)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="app_database"),
        "USER": config("POSTGRES_USER", default="postgres"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="password"),
        "HOST": config("POSTGRES_HOST", default="localhost"),
        "PORT": config("POSTGRES_PORT", default="5432"),
        "OPTIONS": {
            "options": "-c search_path=payment_api"
        },
    }
}


# Static files
STATIC_URL = "static/"

# Stripe settings
if DEBUG:
    STRIPE_PUBLIC_KEY = config("TEST_STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = config("TEST_STRIPE_SECRET_KEY")
else:
    STRIPE_PUBLIC_KEY = config("LIVE_STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY = config("LIVE_STRIPE_SECRET_KEY")


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
