# cloth/urls.py

from django.urls import path
from .views import ProductListView, OrderCreateView, Tag1ListView, Tag2ListView, Tag3ListView, Tag4ListView, MainView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('tag1/', Tag1ListView.as_view(), name='tag1-list'),
    path('tag2/', Tag2ListView.as_view(), name='tag2-list'),
    path('tag3/', Tag3ListView.as_view(), name='tag3-list'),
    path('tag4/', Tag4ListView.as_view(), name='tag4-list'),

]
