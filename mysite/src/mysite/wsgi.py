"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import sys
import os
# add because of error:ImportError: No module named 'mysite'\r
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
