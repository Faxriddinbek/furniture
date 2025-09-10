from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from django.utils.autoreload import autoreload_started

from apps.blog.models import BlogCategory, BlogTags, BlogPost, BlocAuthorModel, BlogViewModel

def blog_page_views(request):
    blogs = BlogPost.objects.filter(
        status=BlogPost.BlogStatus.PUBLISHED
    )
    categories = BlogCategory.objects.all()
    tags = BlogTags.objects.all()
    most_popular_blogs = (
        BlogPost.objects
        .annotate(views_count=Count('views', distinct=True))
        .order_by('-views_count')[:4]
    )

    context = {
        "blogs": blogs,
        "categories": categories,
        "tags": tags,
        "most_popular_blogs": most_popular_blogs,
    }
    return render(
        request, 'blog-list-sidebar-left.html',
        context
    )

def check_blog_view(request, blog):
    # Get user IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        user_ip = x_forwarded_for.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    # Find last view of this blog by this IP
    last_view = BlogViewModel.objects.filter(
        user_ip=user_ip, blog=blog
    ).order_by('-created_at').first()

    # If never viewed OR last view was more than 7 days ago → create new record
    if not last_view or (timezone.now() - last_view.created_at) > timedelta(days=1):
        BlogViewModel.objects.create(user_ip=user_ip, blog=blog)

def blog_detail_page_views(request, pk):
    blog = get_object_or_404(BlogPost, id=pk)
    check_blog_view(request, blog)
    author = BlocAuthorModel.objects.all()

    categories = BlogCategory.objects.all()
    tags = BlogTags.objects.all()

    # related blogs by same categories
    related_blogs = BlogPost.objects.filter(
        category__in=blog.category.all()
    ).exclude(id=blog.id).distinct()

    most_popular_blogs = (
        BlogPost.objects
        .annotate(views_count=Count('views__user_ip', distinct=True))
        .order_by('-views_count')[:4]
    )

    context = {
        "blog": blog,
        "categories": categories,
        "tags": tags,
        "author": author,
        "related_blogs": related_blogs,
        "most_popular_blogs": most_popular_blogs,
    }
    return render(request, 'blog-detail.html', context)