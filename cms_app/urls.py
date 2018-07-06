from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save-theme/$', views.save_theme ,name="save_theme"),
    url(r'^set_thumbnail/$', views.save_thumbnail, name="save_thumbnail"),
    url(r'^get_thambnail/(?P<slug>[\w-]+)/$', views.get_theme ,name="get_theme"),

    # url(r'^save-thumb/$', views.save_thumb, name="save_thumb"),
    url(r'^channel/$', views.room, name='room'),
]