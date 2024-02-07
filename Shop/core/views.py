
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import AddProduct
from .models import Product, Category


def index(request):
    return render(request, 'core/index.html')


def catalog(request):
    categories = Category.objects.all()
    return render(request, 'core/catalog.html', {'categories': categories})


def category_products(request, catalog_id):
    category = get_object_or_404(Category, id=catalog_id)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(request, 'core/products.html', {'category': category, 'products_page': products_page})


def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(request, 'core/products.html', {'products_page': products_page})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:catalog')
    else:
        form = AddProduct()
    return render(request, 'core/add_product.html', {'form': form})

