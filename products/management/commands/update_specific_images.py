from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Updates images for specific products with reliable image URLs'

    def handle(self, *args, **options):
        # Updated image URLs - using reliable direct image sources
        product_images = {
            # Levi's Jeans - jeans image
            "Levi's Jeans": 'https://images.unsplash.com/photo-1542272604-787c1253830b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
            
            # Samsung Galaxy S21 - phone image
            "Samsung Galaxy S21": 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
            
            # Men's Casual Shirt - shirt image
            "Men's Casual Shirt": 'https://images.unsplash.com/photo-1594938291221-94f18e0a5726?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
            
            # Women's Crop Top - women shirt image
            "Women's Crop Top": 'https://images.unsplash.com/photo-1617137968427-85924c800a22?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=500&q=80',
        }
        
        updated_count = 0
        
        for product_name, image_url in product_images.items():
            try:
                products = Product.objects.filter(title=product_name)
                if products.exists():
                    for product in products:
                        product.image_url = image_url
                        product.save()
                        updated_count += 1
                        self.stdout.write(
                            self.style.SUCCESS(f'Updated image for: {product.title}')
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Product not found: {product_name}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error updating {product_name}: {str(e)}')
                )
        
        if updated_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nSuccessfully updated images for {updated_count} product(s)!'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING('No products were updated.')
            )

