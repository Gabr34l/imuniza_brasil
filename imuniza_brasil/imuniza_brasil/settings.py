"""
Django settings for imuniza_brasil project.
"""

from pathlib import Path

# Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Use a chave que o Django gerou aí no seu projeto (mantive a sua para dev)
SECRET_KEY = 'django-insecure-%78%h%1=oto(o(_wf7v3&^x^k8-b*ya5e5m9z^w&cjt#@2fel^'

# Ambiente de desenvolvimento
DEBUG = True
ALLOWED_HOSTS: list[str] = []

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # não precisa registrar 'imuniza_brasil' como app, pois é o pacote do projeto
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

ROOT_URLCONF = 'imuniza_brasil.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # sua pasta de templates está dentro de imuniza_brasil/templates
        'DIRS': [BASE_DIR / 'imuniza_brasil' / 'templates'],
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

WSGI_APPLICATION = 'imuniza_brasil.wsgi.application'

# Banco de dados (SQLite para dev)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validações de senha (padrão)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
# sua pasta de CSS está em imuniza_brasil/css
STATICFILES_DIRS = [BASE_DIR / 'imuniza_brasil' / 'css']

# Chave padrão para PKs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
