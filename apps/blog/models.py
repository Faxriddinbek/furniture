from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from apps.product.models import BaseModel

class BlogCategory(BaseModel):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'

class BlogTags(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog tags'
        verbose_name_plural = 'Blog tags'

class BlocAuthorModel(BaseModel):
    full_name = models.CharField(max_length=64)
    image = models.ImageField(
        upload_to='blog-author/'
    )
    bio = models.CharField(max_length=256)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Blog author'
        verbose_name_plural = 'Blog authors'


class BlogPost(BaseModel):
    class BlogStatus(models.TextChoices):
        DRAFT = 'DRAFT'
        PUBLISHED = 'PUBLISHED'
        DELETED = 'DELETED'

    status = models.CharField(
        max_length=20,
        choices=BlogStatus,
        default=BlogStatus.DRAFT
    )

    def views_count(self):
        return self.views.distinct().count()
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    category = models.ManyToManyField(BlogCategory, related_name='blogs')

    tag = models.ManyToManyField(
        BlogTags,
        related_name='blogs'
    )
    author = models.ForeignKey(
        BlocAuthorModel,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class BlogViewModel(BaseModel):
    user_ip = models.CharField(max_length=15)
    blog = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='views'
    )

    def __str__(self):
        return f"{self.user_ip} - {self.blog.id}"

    class Meta:
        verbose_name = 'Blog view'
        verbose_name_plural = 'Blog views'