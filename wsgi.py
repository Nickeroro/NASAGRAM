"""
WSGI config for NASAGRAM project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import sys
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'NASAGRAM')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NASAGRAM.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()



