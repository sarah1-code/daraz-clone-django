from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Adds image URLs to products that don\'t have images'

    def handle(self, *args, **options):
        # Default images for products without images
        default_images = {
            'Electronics': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=500&h=500&fit=crop',
            'Fashion': 'https://images.unsplash.com/photo-1445205170230-053b83016050?w=500&h=500&fit=crop',
            'Gaming': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500&h=500&fit=crop',
            'Home & Living': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop',
            'Sports': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=500&fit=crop',
            'Baby & Kids': 'https://images.unsplash.com/photo-1555255705-5ad0b0e8b0e0?w=500&h=500&fit=crop',
        }
        
        # Get products without images
        products_without_images = Product.objects.filter(
            image__isnull=True,
            image_url__isnull=True
        ) | Product.objects.filter(
            image='',
            image_url__isnull=True
        ) | Product.objects.filter(
            image__isnull=True,
            image_url=''
        )
        
        updated_count = 0
        for product in products_without_images:
            # Use category-based default image
            if product.category in default_images:
                product.image_url = default_images[product.category]
            else:
                # Generic product image
                product.image_url = 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop'
            
            product.save()
            updated_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✓ Added image to: {product.title}')
            )
        
        if updated_count == 0:
            self.stdout.write(
                self.style.SUCCESS('✅ All products already have images!')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n✅ Successfully added images to {updated_count} products!'
                )
            )

