from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
