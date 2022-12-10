from pathlib import Path

# import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'django-insecure-i5v#@#3v@=mku9267fq%m39_zp_c6lqeqsq5a4l3=^zb5b%7c@'

DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'yourdomain.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'widget_tweaks',
    'django_bootstrap5',
    # 'crispy_forms',
    'Store',
    'Cart',
    'Account',
    'Payment'
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Store.context_processors.categories',
                'Cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Core.wsgi.application'


# Database

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'swub!m5Rrs5RNMB',
    'HOST': 'db.hxddevwgtirgybymsyap.supabase.co',
    'PORT': '5432',
  }
}



# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static/'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type

# Crispy templates
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Basket session ID
BASKET_SESSION_ID = 'basket'

# Custom Auth User:
AUTH_USER_MODEL = 'Account.UserBase'
LOGIN_REDIRECT_URL = '/customer/dashboard'
LOGIN_URL = '/customer/login/'


# Pass reset
PASSWORD_RESET_TIMEOUT_DAYS = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

