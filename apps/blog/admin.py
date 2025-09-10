from django.contrib import admin
from .models import BlogCategory, BlogTags, BlocAuthorModel, BlogPost, BlogViewModel
from modeltranslation.admin import TranslationAdmin

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(BlogCategory)
class BlogCategoryAdmin(MyTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)


@admin.register(BlogTags)
class BlogTagsAdmin(MyTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)


@admin.register(BlocAuthorModel)
class BlocAuthorModelAdmin(MyTranslationAdmin):
    list_display = ("id", "full_name", "bio", "image")
    search_fields = ("full_name",)
    list_filter = ("created_at",)


@admin.register(BlogPost)
class BlogPostAdmin(MyTranslationAdmin):
    list_display = ("id", "title", "created_at", "status")
    search_fields = ("title", "content")
    list_filter = ("created_at", "status")

@admin.register(BlogViewModel)
class BlogViewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'blog__title', 'created_at']
    search_fields = ['user_ip']
    list_filter = ['created_at', 'user_ip']
