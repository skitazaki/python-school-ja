DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'template1',
        'USER': 'DB_USER_NAME',
        'PASSWORD': 'DB_USER_PASSWORD',
        'HOST': 'DB_HOST',
        'PORT': int('5432'),
    },
    'staging': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'template1',
        'USER': 'DB_USER_NAME_STAGING',
        'PASSWORD': 'DB_USER_PASSWORD_STAGING',
        'HOST': 'DB_HOST_STAGING',
        'PORT': int('5432'),
    }
}
