from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts app handles home, login, register, profile
    path('', include('accounts.urls')),

    # top-level app URLs
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),      # keep these files even if empty for now
    path('orders/', include('orders.urls')),
]

# serve media in DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
