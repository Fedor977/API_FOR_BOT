from django.urls import path
from .views import category_list, products_category, product_detail

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/<slug:category_slug>/', products_category, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
]

