if not DEBUG:
    INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'south', no longer supported
    'accounts',
    'carts',
    'marketing',
    'orders',
    'products',
    'localflavor',
    )
    
    try:
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()
    except:
        pass    

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    #MEDIA_ROOT = '/Users/jmitch/Desktop/ecommerce/static/media/'

    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )