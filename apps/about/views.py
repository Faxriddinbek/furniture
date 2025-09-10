from django.shortcuts import render

def home_page_views(request):
    return render(request, 'home3.html')
def page_404_views(request):
    return render(request, '404.html')
def about_page_views(request):
    return render(request, 'about-us.html')
