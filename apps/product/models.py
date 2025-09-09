from datetime import datetime
from django.db import models

from apps.about.models import BaseModel


class ProductCategory(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'


class ProductCatalog(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product Catalog'
        verbose_name_plural = 'product Catalog'


class ProductColor(models.Model):
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product color'
        verbose_name_plural = 'product colors'


class ProductTag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product title'
        verbose_name_plural = 'product title'


class ProductModel(BaseModel):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(ProductCategory, related_name='products')
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
