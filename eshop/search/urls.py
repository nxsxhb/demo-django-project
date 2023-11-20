from . import views
from eshop import settings
from django.conf.urls.static import static
from django.urls import path
app_name='search'

urlpatterns = [
    path('', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)