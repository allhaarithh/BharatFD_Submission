# faq_project/settings.py
INSTALLED_APPS = [
    # ...
    'ckeditor',
    'rest_framework',
    'faq_management',
]

# Redis Cache Configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# CKEditor Configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
    }
}