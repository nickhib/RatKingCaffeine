from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
#    re_path(r"ws/home/CoffeeDirectory/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/CoffeeDirectory/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    ]
