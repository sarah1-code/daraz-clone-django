from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Fixes all product images with reliable image URLs'

    def handle(self, *args, **options):
        # Better image URLs - using reliable sources
        product_image_map = {
            # Electronics
            'Samsung Galaxy S21': 'https://images.unsplash.com/photo-1610945265064-0e34e5519bbd?w=500&h=500&fit=crop&auto=format',
            'MacBook Pro 16"': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=500&h=500&fit=crop&auto=format',
            'Wireless Bluetooth Headphones': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop&auto=format',
            'Smart Watch': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&h=500&fit=crop&auto=format',
            'LED TV 55 inch': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop&auto=format',
            
            # Gaming
            'Gaming Mouse': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&h=500&fit=crop&auto=format',
            'Gaming Keyboard': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&h=500&fit=crop&auto=format',
            'PlayStation 5': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500&h=500&fit=crop&auto=format',
            'Gaming Headset': 'https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop&auto=format',
            
            # Fashion - Shoes
            'Nike Air Max Running Shoes': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop&auto=format',
            'Adidas Sports Shoes': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500&h=500&fit=crop&auto=format',
            'Leather Formal Shoes': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=500&h=500&fit=crop&auto=format',
            'Casual Sneakers': 'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=500&h=500&fit=crop&auto=format',
            
            # Fashion - Clothes
            "Levi's Jeans": 'https://images.unsplash.com/photo-1542272604-787c1253830b?w=500&h=500&fit=crop&auto=format',
            'Cotton T-Shirt Pack': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop&auto=format',
            
            # Men's Shirts
            "Men's Casual Shirt": 'https://images.unsplash.com/photo-1594938291221-94f18e0a5726?w=500&h=500&fit=crop&auto=format',
            "Men's Formal Shirt": 'https://images.unsplash.com/photo-1603252109303-2751441dd157?w=500&h=500&fit=crop&auto=format',
            "Men's Polo Shirt": 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop&auto=format',
            "Men's Checkered Shirt": 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop&auto=format',
            "Men's Denim Shirt": 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop&auto=format',
            
            # Women's Shirts
            "Women's Floral Shirt": 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop&auto=format',
            "Women's Casual T-Shirt": 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500&h=500&fit=crop&auto=format',
            "Women's Blouse": 'https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=500&h=500&fit=crop&auto=format',
            "Women's Off-Shoulder Top": 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop&auto=format',
            "Women's Crop Top": 'https://images.unsplash.com/photo-1617137968427-85924c800a22?w=500&h=500&fit=crop&auto=format',
            "Women's Striped Shirt": 'https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=500&h=500&fit=crop&auto=format',
            
            # Home & Living
            'Coffee Maker Machine': 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?w=500&h=500&fit=crop&auto=format',
            'Dining Table Set': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop&auto=format',
            'Sofa Set': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&h=500&fit=crop&auto=format',
            'Bedroom Wardrobe': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop&auto=format',
            
            # Sports
            'Yoga Mat': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&h=500&fit=crop&auto=format',
            'Dumbbell Set': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=500&fit=crop&auto=format',
            'Basketball': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=500&h=500&fit=crop&auto=format',
            
            # Baby & Kids
            'Baby Stroller': 'https://images.unsplash.com/photo-1555255705-5ad0b0e8b0e0?w=500&h=500&fit=crop&auto=format',
            'Kids Bicycle': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&h=500&fit=crop&auto=format',
        }
        
        updated_count = 0
        not_found = []
        
        # Update all products
        all_products = Product.objects.all()
        for product in all_products:
            if product.title in product_image_map:
                product.image_url = product_image_map[product.title]
                product.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated: {product.title}')
                )
            else:
                # For products not in map, use category-based default
                if not product.image_url or not product.image_url.strip():
                    category_images = {
                        'Electronics': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=500&h=500&fit=crop&auto=format',
                        'Fashion': 'https://images.unsplash.com/photo-1445205170230-053b83016050?w=500&h=500&fit=crop&auto=format',
                        'Gaming': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500&h=500&fit=crop&auto=format',
                        'Home & Living': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop&auto=format',
                        'Sports': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=500&fit=crop&auto=format',
                        'Baby & Kids': 'https://images.unsplash.com/photo-1555255705-5ad0b0e8b0e0?w=500&h=500&fit=crop&auto=format',
                    }
                    if product.category in category_images:
                        product.image_url = category_images[product.category]
                        product.save()
                        updated_count += 1
                        self.stdout.write(
                            self.style.SUCCESS(f'Added default image to: {product.title}')
                        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully updated {updated_count} product(s) with images!'
            )
        )
        
        # Check for products still without images
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
        
        if products_without_images.exists():
            self.stdout.write(
                self.style.WARNING(
                    f'\nWarning: {products_without_images.count()} product(s) still without images:'
                )
            )
            for p in products_without_images:
                self.stdout.write(f'  - {p.title}')

