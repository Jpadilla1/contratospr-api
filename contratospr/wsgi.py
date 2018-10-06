"""
WSGI config for contratospr project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os

configuration = os.getenv("ENVIRONMENT", "development").title()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contratospr.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", configuration)

from configurations.wsgi import get_wsgi_application  # noqa isort:skip

application = get_wsgi_application()
