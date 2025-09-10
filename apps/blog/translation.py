from modeltranslation.decorators import register
from modeltranslation.translator import  TranslationOptions
from apps.blog.models import BlogPost, BlogTags, BlogCategory, BlocAuthorModel


@register(BlogPost)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(BlogTags)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(BlogCategory)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(BlocAuthorModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio')