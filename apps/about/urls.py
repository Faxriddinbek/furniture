from django.urls import path
from .views import home_page_views, page_404_views, about_page_views, blog_detail_page_views, blog_list_page_views, product_page_views
app_name = 'about'

urlpatterns = [
    path('', home_page_views, name = 'home'),
    path('404/', page_404_views, name = '404'),
    path('about/', about_page_views, name = 'abouts'),
    path('blog-detail/', blog_detail_page_views, name = 'blog_detail'),
    path('blog-lis/', blog_list_page_views, name = 'blog-list'),
    # path('product/', product_page_views, name = 'product'),
]