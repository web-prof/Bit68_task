from django.urls import path
from .views import *


app_name = 'products'
urlpatterns = [
    path('', get_post_products.as_view(), name='get_post_products'),
    path('<int:pk>/', get_update_delete_product.as_view(),
         name='get_update_delete_product'),
]
