from django.urls import path

from .views import product_pages_views
app_name = 'product'
urlpatterns = [
    path('', product_pages_views, name = 'products')
]