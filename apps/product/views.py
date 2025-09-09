from django.shortcuts import render

from apps.product.models import ProductCategory, ProductCatalog, ProductColor, ProductTag, ProductModel


def product_pages_views(request):
    categories = ProductCategory.objects.all()
    catalog = ProductCatalog.objects.all()
    colors = ProductColor.objects.all()
    tags = ProductTag.objects.all()
    products = ProductModel.objects.all()

    context = {
            "categories": categories,
            "catalog": catalog,
            "colors": colors,
            "tags": tags,
            "products": products,
        }

    return render(request, 'product-grid-sidebar-left.html', context)