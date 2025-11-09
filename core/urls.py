from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view
def home(request):
    return HttpResponse("<h1>Welcome to Daraz Clone 🛍️</h1><p>Project under development</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          # <-- This is the homepage
    path('', include('accounts.urls')),   # keep accounts URLs
]
