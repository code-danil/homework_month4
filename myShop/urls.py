from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_view, name='category_list'),
    path('products/<int:category_id>/', views.products_view, name='category_products'),
]