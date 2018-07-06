from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/theme/channel/$', consumers.ChatConsumer),
]