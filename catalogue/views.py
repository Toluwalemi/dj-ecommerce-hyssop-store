from django.shortcuts import render

# Create your views here.
from catalogue.models import Category, Product


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(
        request,
        'product/list.html',
        {
            'categories': categories,
            'products': products
        }
    )
