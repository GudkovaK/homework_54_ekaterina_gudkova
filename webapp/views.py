from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    return render(request, 'webapp/products.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'webapp/product.html', {'product': product})


def product_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category_id = request.POST.get('category')
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
            category_id=category_id
        )
        return redirect('product_view', pk=product.pk)
    categories = Category.objects.all()
    return render(request, 'webapp/product_add.html', {'categories': categories})


def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('products_view')
    return render(request, 'webapp/category_add.html')
