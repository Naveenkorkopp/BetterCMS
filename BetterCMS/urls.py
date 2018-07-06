from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^th/', include('cms_app.urls')),
    url(r'^admin/', admin.site.urls),
]