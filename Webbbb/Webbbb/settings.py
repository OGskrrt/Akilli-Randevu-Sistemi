"""
Django settings for Webbbb project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/



Https server start command
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:8000


"""

from pathlib import Path
import os
import allauth

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s94wyya9+6z9d4b647=n!-&uiweg=b9gshzv=rkgfm*fdl4rdo'
# Django'da SECRET_KEY yönetimi, uygulamanın güvenliği açısından kritik bir adımdır.
# SECRET_KEY, Django'nun çeşitli güvenlik mekanizmalarında,
# özellikle oturumlar (sessions), CSRF tokenleri ve şifreleme işlemlerinde kullanılır.
# Bu anahtarın güvenli ve rastgele oluşturulmuş olması, uygulamanızın güvenliğini sağlamada
# büyük önem taşır.


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Debug modunda üretim sırasında hata ayrıntılarının dışarı sızmasını önler
# debug modunu kapatarak aslında release modu açmış oluyoruz. bu sayede üretim yaparken çıkan hata
# detaylı hata kodlarının sızılmasını önlüyoruz. Bu şekilde günveliğin yanında performans da kazanmış oluyoruz.

# debug false ayarında allowed hosts da yapılamalı
# ALLOWED_HOSTS = ['example.com', 'www.example.com', '192.168.1.1']
# gibi. Bu şekilde sadece yazılan domainler kontrol edilecek
# dommain olmadığı için şimdilik boş bırakıyoruz
ALLOWED_HOSTS = ['*']

 # client id 83009058085-fvghunjub18repros5s65gdg93r375ma.apps.googleusercontent.com
 # client secret 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


# Application definition

INSTALLED_APPS = [
    'mainapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'django_createsuperuserwithpassword',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework_simplejwt',

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# 'django_extensions' uygulaması ile HTTPS protokolu kullanılabilir.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = 'vatandas/home/'

LOGOUT_REDIRECT_URL = 'vatandas/giris'

# Django, CSRF ara yazılımı aracılığıyla CSRF saldırılarına karşı yerleşik koruma sağlar.
# 'django.middleware.csrf.CsrfViewMiddleware' ile sağlanır

ROOT_URLCONF = 'Webbbb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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





WSGI_APPLICATION = 'Webbbb.wsgi.application'




# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# myproject/settings.py

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Static files configuration for deployment
STATIC_ROOT = BASE_DIR / "staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py


# Kullanımlarını aynı siteden gelen isteklerle sınırlamak için oturum çerezlerinizin
# SameSite özelliğini ayarlayın. Bu, kullanıcının tarayıcısının siteler arası isteklerle birlikte
# oturum çerezini göndermesini engelleyerek CSRF saldırılarını etkili bir şekilde azaltır.
# SESSION_COOKIE_SAMESITE = 'Strict'  # or 'Lax'

# SECURE_SSL_REDIRECT = True  # HTTP'den HTTPS'ye yönlendirme
# CSRF_COOKIE_SECURE = True  # CSRF çerezlerini güvenli yapar
# SESSION_COOKIE_SECURE = True  # Oturum çerezlerini güvenli yapar
# # SECURE_HSTS_SECONDS = 3600  # HSTS etkinleştirme ve süresi
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Alt alan adları için HSTS
# SECURE_HSTS_PRELOAD = True  # HSTS preload listesine ekleme
# SECURE_BROWSER_XSS_FILTER = True  # Tarayıcı XSS koruması
# X_FRAME_OPTIONS = 'DENY'  # Clickjacking koruması
# # X_FRAME_OPTIONS = 'SAMEORIGIN'
# SECURE_CONTENT_TYPE_NOSNIFF = True # İçerik türü hilelerine karşı koruma sağlamak için


SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Varsayılan ayar
SESSION_COOKIE_NAME = 'sessionid'  # Varsayılan oturum çerez adı

