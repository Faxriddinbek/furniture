from django.contrib import admin

from .models import (
    ProductCategory, ProductCatalog, ProductColor, ProductTag,
    ProductModel
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)


@admin.register(ProductCatalog)
class ProductCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "code")
    search_fields = ("title", "code")


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "quantity", "color")
    list_filter = ("categories", "color")
    search_fields = ("title",)
    filter_horizontal = ("categories",)