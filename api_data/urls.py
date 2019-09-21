from django.urls import path
from . import views

urlpatterns = [
    path('get_stock_data', views.get_stock_data, name="get_stock_data"),
    path('get_purchase_data', views.get_purchase_data, name="get_purchase_data"),
    path('get_sale_data', views.get_sale_data, name="get_sale_data"),
    path('get_product_data', views.get_product_data, name="get_product_data"),
]
