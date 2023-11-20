from . import views
from eshop import settings
from django.conf.urls.static import static
from django.urls import path
app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove, name='cart_remove'),
    path('delete/<int:product_id>/',views.cart_delete, name='cart_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)