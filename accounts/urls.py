from django.urls import path
from . import views

urlpatterns = [
    # home (protected in views.py with @login_required)
    path('', views.home, name='home'),

    # authentication views
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    
    # profile (protected)
    path('profile/', views.profile, name='profile'),
]
