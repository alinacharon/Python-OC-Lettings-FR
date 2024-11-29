from django.contrib import admin
from django.urls import include, path

from . import views
from django.conf.urls import handler404, handler500

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
