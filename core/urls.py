from django.urls import path

from .views import category_list, products_category

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('products/<int:category_id>/', products_category, name='products_list')
]