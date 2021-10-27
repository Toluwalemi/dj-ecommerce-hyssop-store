from django.urls import path

from .views import product_list

app_name = 'catalogues'
urlpatterns = [
    path('', product_list, name='product_list'),
]
