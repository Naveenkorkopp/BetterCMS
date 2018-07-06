from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chat/$', views.index, name='index'),
    url(r'^save-theme/$', views.save_theme ,name="save_theme"),
    url(r'^save-thumb/$', views.save_thumb, name="save_thumb"),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]