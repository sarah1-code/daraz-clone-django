from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Updates images for specific products (Levi\'s Jeans, Men\'s Casual Shirt, Men\'s Checkered Shirt)'

    def handle(self, *args, **options):
        # Product images mapping - using better quality product images
        product_images = {
            "Levi's Jeans": 'https://images.unsplash.com/photo-1542272604-787c1253830b?w=500&h=500&fit=crop',
            "Men's Casual Shirt": 'https://images.unsplash.com/photo-1594938291221-94f18e0a5726?w=500&h=500&fit=crop',
            "Men's Checkered Shirt": 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop',
        }
        
        updated_count = 0
        
        for product_name, image_url in product_images.items():
            try:
                product = Product.objects.get(title=product_name)
                product.image_url = image_url
                product.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated image for: {product_name}')
                )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Product not found: {product_name}')
                )
            except Product.MultipleObjectsReturned:
                # If multiple products with same name, update all
                products = Product.objects.filter(title=product_name)
                for product in products:
                    product.image_url = image_url
                    product.save()
                updated_count += len(products)
                self.stdout.write(
                    self.style.SUCCESS(f'Updated {len(products)} product(s) with name: {product_name}')
                )
        
        if updated_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nSuccessfully updated images for {updated_count} product(s)!'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING('No products were updated. Make sure the products exist.')
            )

