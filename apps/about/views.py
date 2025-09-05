from django.shortcuts import render

def home_page_views(request):
    return render(request, 'home3.html')
def page_404_views(request):
    return render(request, '404.html')
def about_page_views(request):
    return render(request, 'about-us.html')
def blog_detail_page_views(request):
    return render(request, 'blog-detail.html')
def blog_list_page_views(request):
    return render(request, 'blog-list-sidebar-left.html')
def product_page_views(request):
    return render(request, 'product-cart.html')
