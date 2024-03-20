"""
ASGI config for homepage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

# import django
# from channels.http import AsgiHandler

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homepage.settings')

#django.setup()
#application = ProtocolTypeRouter(
     #   {
      #      "http": = get_asgi_application(),

       # }

#)
django_asgi_app = get_asgi_application()
import home.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        #"http": AsgiHandler(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(home.routing.websocket_urlpatterns))
        ),
    }
)
