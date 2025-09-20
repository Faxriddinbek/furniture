from django.urls import path

app_name = 'accounts'
from apps.accounts.views import RegisterCreateView, LoginFormView

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
]