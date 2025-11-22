from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart_detail')

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.total_price
        )
    cart_items.delete()  # empty cart after order
    return render(request, 'orders/checkout_success.html')

@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})
