from . import views
from django.urls import path,include
from eshop import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
    path('cart/', include('cart.urls')),
    path('search/',include('search.urls')), 
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name ='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetails, name ='proDetails'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)