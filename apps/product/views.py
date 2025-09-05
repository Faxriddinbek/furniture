from django.shortcuts import render

def product_pages_views(request):
    return render(request, 'product-grid-sidebar-left.html')