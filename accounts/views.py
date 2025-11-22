from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# REGISTER VIEW
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        
        # Auto-login after registration
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after auto-login

    return render(request, 'accounts/register.html')


# LOGIN VIEW
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')


# LOGOUT VIEW
def logout_user(request):
    logout(request)
    return redirect('login')


# HOME VIEW (Protected)
@login_required(login_url='login')
def home(request):
    from products.models import Product
    from django.db.models import Q
    
    # Get all products to display on home page
    products = Product.objects.all()[:8]  # Show first 8 products
    
    # Get shirts for "Just For You" section (men's and women's shirts, tops, blouses)
    just_for_you_products = Product.objects.filter(
        Q(title__icontains='shirt') | 
        Q(title__icontains='Shirt') | 
        Q(title__icontains='Top') | 
        Q(title__icontains='Blouse')
    ).filter(category='Fashion')
    
    # If not enough shirts, add more fashion products
    shirt_count = just_for_you_products.count()
    if shirt_count < 12:
        additional = Product.objects.filter(category='Fashion').exclude(
            id__in=just_for_you_products.values_list('id', flat=True)
        )[:12 - shirt_count]
        just_for_you_products = list(just_for_you_products) + list(additional)
    
    # If still not enough, add random products
    if len(just_for_you_products) < 12:
        shirt_ids = [p.id for p in just_for_you_products]
        remaining = Product.objects.exclude(id__in=shirt_ids)[:12 - len(just_for_you_products)]
        just_for_you_products = list(just_for_you_products) + list(remaining)
    
    return render(request, 'accounts/home.html', {
        'products': products,
        'just_for_you_products': just_for_you_products[:12]
    })


# PROFILE VIEW (Protected)
@login_required(login_url='login')
def profile(request):
    from accounts.models import Profile
    from orders.models import Order
    
    # Get or create profile
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Get user's orders
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    
    # Calculate total payments (sum of all order prices)
    total_payments = sum(order.total_price for order in orders)
    
    context = {
        'profile': profile,
        'orders': orders,
        'total_payments': total_payments,
    }
    return render(request, 'accounts/profile.html', context)
