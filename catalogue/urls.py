from django.urls import path

from .views import product_list

app_name = 'catalogues'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>', product_list, name='product_list_by_category'),
]