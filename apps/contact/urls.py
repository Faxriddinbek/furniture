from django.urls import path
from .views import contact_page_views
app_name = 'contact'

urlpatterns = [
    path('', contact_page_views, name = 'contacts')
]