from django.urls import path
from .views import get_category,create_category,detail_category,delete_category,product_create,product_search_view

urlpatterns = [
    # category crud
    path('',get_category,  name='category-list'),
    path('create/',create_category,  name='category-create'),
    path('create/<int:pk>/',detail_category,  name='category-detail'),
    path('delete/<int:pk>/',delete_category,  name='category-delete'),

    # product crud
    path('pro-list/',product_search_view,name='product-list'),
    path('pro-create/',product_create,name='product-create'),

]