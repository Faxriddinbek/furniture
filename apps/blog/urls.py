from django.urls import path

from apps.blog.views import blog_page_views, blog_detail_page_views

app_name = 'blogs'

urlpatterns = [
        path('product/', blog_page_views, name = 'blog'),
        path('<int:pk>/', blog_detail_page_views, name='blog-detail'),
]