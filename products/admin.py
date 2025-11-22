from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'category')
    ordering = ('title',)
    
    fieldsets = (
        ('Product Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Pricing', {
            'fields': ('price',)
        }),
        ('Image', {
            'fields': ('image', 'image_url')
        }),
    )
