from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

# product list (protected)
@login_required(login_url='login')
def product_list(request):
    category = request.GET.get('category', None)
    if category:
        products = Product.objects.filter(category__iexact=category)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'selected_category': category
    })

# category products view
@login_required(login_url='login')
def category_products(request, category):
    products = Product.objects.filter(category__iexact=category)
    return render(request, 'products/product_list.html', {
        'products': products,
        'selected_category': category,
        'category_name': category
    })

# product detail (protected)
@login_required(login_url='login')
def product_detail(request, pk):
    from reviews.models import Review
    p = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=p)[:10]  # Get latest 10 reviews
    return render(request, 'products/product_detail.html', {
        'product': p,
        'reviews': reviews
    })
