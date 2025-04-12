from django.shortcuts import render,redirect

from page.forms import CategoryForm, ProductForm
from page.models import Category, Product

from django.shortcuts import render
from django.db.models import Q
from .models import Product

def product_search_view(request):
    query = request.GET.get('q')  # foydalanuvchi yozgan so‘z
    results = Product.objects.all()

    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(price__icontains=query)
        )

    return render(request, 'products/product_list.html', {'products': results, 'query': query})

def get_category(request):
    cats = Category.objects.all()
    return render(request, 'products/category.html', {'cats': cats})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})


def detail_category(request, pk):
    cat = Category.objects.get(pk=pk)
    return render(request, 'products/category_detail.html', {'cat': cat})


def delete_category(request,pk):

    category = Category.objects.get(pk=pk)
    category.delete()
    if category is None:
        return redirect('category-list')
    else:

        return render(request, 'products/delete_category.html', {'category': category})




def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})




