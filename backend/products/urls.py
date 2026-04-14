from django.urls import path
from . import views

urlpatterns = [
    path('getProducts/', views.get_products),
    path('getProductById/<int:id>/', views.get_product_by_id),
    path('getProductByName/<str:name>/', views.get_product_by_name),
    path('add/', views.create_product),
    path('update/<int:id>/', views.update_product),
    path('delete/<int:id>/', views.delete_product),
]