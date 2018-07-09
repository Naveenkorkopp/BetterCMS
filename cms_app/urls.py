from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save-theme/$', views.save_theme ,name="save_theme"),
    url(r'^set_thumbnail/$', views.save_thumbnail, name="save_thumbnail"),
    url(r'^get_thumbnails/$', views.get_thumbnail, name="get_thumbnail"),
    url(r'^get_theme/$', views.get_theme ,name="get_theme"),

    url(r'^userData/$', views.get_dummyData, name='get_dummyData'),
    url(r'^itemData/$', views.get_dummyData2, name='get_dummyData2'),
    url(r'^countryData/$', views.get_dummyData3, name='get_dummyData3'),

    # url(r'^get_theme/(?P<slug>[\w-]+)/$', views.get_theme ,name="get_theme"),

    # url(r'^save-thumb/$', views.save_thumb, name="save_thumb"),
    
    url(r'^channel/$', views.room, name='room'), # Web-Socket channel connect Api
]