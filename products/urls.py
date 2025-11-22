from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
