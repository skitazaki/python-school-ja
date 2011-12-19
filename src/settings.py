DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'template1',
        'USER': 'DOTCLOUD_DB_SQL_LOGIN',
        'PASSWORD': 'DOTCLOUD_DB_SQL_PASSWORD',
        'HOST': 'DOTCLOUD_DB_SQL_HOST',
        'PORT': int('12345'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
