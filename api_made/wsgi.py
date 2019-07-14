"""
WSGI config for api_made project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
# import os
# from whitenoise import WhiteNoise
#
# from django.core.wsgi import get_wsgi_application
#
#
# application = get_wsgi_application()
# application = WhiteNoise(application, root='/path/to/static/files')
# application.add_files('/path/to/more/static/files', prefix='more-files/')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_made.settings')
#






import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_made.settings')

application = get_wsgi_application()
