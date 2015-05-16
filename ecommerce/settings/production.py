if not DEBUG:
    try:
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()
    except:
        pass    

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
