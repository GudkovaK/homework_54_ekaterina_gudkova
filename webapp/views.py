from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category
from webapp.forms import ProductForm


def products_view(request):
    products = Product.objects.filter(stock__gte=1).order_by('category__name', 'name')
    return render(request, 'webapp/products.html', {'products': products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'webapp/product.html', {'product': product})

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                image=form.cleaned_data['image'],
                category_id=form.cleaned_data['category'],
                stock=form.cleaned_data['stock']
            )
            return redirect('product_view', pk=product.pk)
    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'webapp/product_add.html', {'form': form, 'categories': categories})

def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.image = form.cleaned_data['image']
            product.category_id = form.cleaned_data['category']
            product.stock = form.cleaned_data['stock']
            product.save()
            return redirect('product_view', pk=product.pk)
    else:
        form = ProductForm(initial={
            'name': product.name,
            'description':product.description,
            'price': product.price,
            'image': product.image,
            'category': product.category_id,
            'stock': product.stock
        })
    categories = Category.objects.all()
    return render(request,'webapp/product_edit.html', {'form': form, 'categories': categories, 'product': product})

def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method =='POST':
        product.delete()
        return redirect('product_view')
    return render(request, 'webapp/product_delete.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('products_view')
    return render(request, 'webapp/category_add.html')
