from django.core.management.base import BaseCommand
from products.models import Product
import random


class Command(BaseCommand):
    help = 'Adds sample products to the database with images'

    def handle(self, *args, **options):
        # Sample products data with image URLs
        products_data = [
            # Electronics
            {
                'title': 'Samsung Galaxy S21',
                'price': 85000.00,
                'original_price': 95000.00,
                'description': 'Latest Samsung smartphone with amazing camera and 5G support. Perfect for photography enthusiasts.',
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            },
            {
                'title': 'MacBook Pro 16"',
                'price': 250000.00,
                'original_price': 280000.00,
                'description': 'Powerful laptop for professionals. M1 chip, 16GB RAM, perfect for developers and designers.',
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=500&h=500&fit=crop',
            },
            {
                'title': 'Wireless Bluetooth Headphones',
                'price': 5000.00,
                'original_price': 7000.00,
                'description': 'High-quality noise-cancelling headphones with 30-hour battery life.',
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop',
            },
            {
                'title': 'Smart Watch',
                'price': 18000.00,
                'original_price': 22000.00,
                'description': 'Fitness tracker with heart rate monitor, GPS, and smartphone notifications.',
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&h=500&fit=crop',
            },
            {
                'title': 'LED TV 55 inch',
                'price': 75000.00,
                'original_price': 90000.00,
                'description': '4K Ultra HD Smart TV with HDR support. Perfect for home entertainment.',
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop',
            },
            {
                'title': 'Gaming Mouse',
                'price': 3500.00,
                'original_price': 4500.00,
                'description': 'RGB gaming mouse with high precision sensor. Perfect for gamers.',
                'category': 'Gaming',
                'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&h=500&fit=crop',
            },
            {
                'title': 'Gaming Keyboard',
                'price': 8000.00,
                'original_price': 10000.00,
                'description': 'Mechanical gaming keyboard with RGB backlight. Fast response time.',
                'category': 'Gaming',
                'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&h=500&fit=crop',
            },
            {
                'title': 'PlayStation 5',
                'price': 120000.00,
                'original_price': 150000.00,
                'description': 'Latest gaming console with 4K gaming support. Includes controller.',
                'category': 'Gaming',
                'image_url': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500&h=500&fit=crop',
            },
            {
                'title': 'Gaming Headset',
                'price': 12000.00,
                'original_price': 15000.00,
                'description': '7.1 surround sound gaming headset with noise cancellation.',
                'category': 'Gaming',
                'image_url': 'https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop',
            },
            # Fashion - Shoes
            {
                'title': 'Nike Air Max Running Shoes',
                'price': 12000.00,
                'original_price': 15000.00,
                'description': 'Comfortable running shoes with air cushioning. Perfect for daily workouts and jogging.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop',
            },
            {
                'title': 'Adidas Sports Shoes',
                'price': 10000.00,
                'original_price': 13000.00,
                'description': 'Lightweight sports shoes with excellent grip. Perfect for running and training.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500&h=500&fit=crop',
            },
            {
                'title': 'Leather Formal Shoes',
                'price': 8000.00,
                'original_price': 10000.00,
                'description': 'Premium leather formal shoes. Perfect for office and formal occasions.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=500&h=500&fit=crop',
            },
            {
                'title': 'Casual Sneakers',
                'price': 5000.00,
                'original_price': 7000.00,
                'description': 'Comfortable casual sneakers for everyday wear. Available in multiple colors.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=500&h=500&fit=crop',
            },
            {
                'title': 'Levi\'s Jeans',
                'price': 3500.00,
                'original_price': 4500.00,
                'description': 'Classic fit denim jeans. Comfortable and stylish for everyday wear.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1542272604-787c1253830b?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            },
            {
                'title': 'Cotton T-Shirt Pack',
                'price': 2000.00,
                'original_price': 3000.00,
                'description': 'Pack of 3 comfortable cotton t-shirts. Available in multiple colors.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop',
            },
            # Home & Living
            {
                'title': 'Coffee Maker Machine',
                'price': 15000.00,
                'original_price': 20000.00,
                'description': 'Automatic coffee maker with programmable timer. Make perfect coffee every morning.',
                'category': 'Home & Living',
                'image_url': 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?w=500&h=500&fit=crop',
            },
            {
                'title': 'Dining Table Set',
                'price': 45000.00,
                'original_price': 55000.00,
                'description': 'Modern 6-seater dining table with chairs. Perfect for family gatherings.',
                'category': 'Home & Living',
                'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop',
            },
            {
                'title': 'Sofa Set',
                'price': 85000.00,
                'original_price': 100000.00,
                'description': 'Comfortable 3-seater sofa set with cushions. Modern design.',
                'category': 'Home & Living',
                'image_url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&h=500&fit=crop',
            },
            {
                'title': 'Bedroom Wardrobe',
                'price': 35000.00,
                'original_price': 45000.00,
                'description': 'Spacious wardrobe with sliding doors. Perfect for bedroom storage.',
                'category': 'Home & Living',
                'image_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&h=500&fit=crop',
            },
            # Sports
            {
                'title': 'Yoga Mat',
                'price': 2500.00,
                'original_price': 3500.00,
                'description': 'Non-slip yoga mat with carrying strap. Perfect for yoga and exercise.',
                'category': 'Sports',
                'image_url': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&h=500&fit=crop',
            },
            {
                'title': 'Dumbbell Set',
                'price': 15000.00,
                'original_price': 20000.00,
                'description': 'Adjustable dumbbell set 5-25kg. Perfect for home workouts.',
                'category': 'Sports',
                'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=500&fit=crop',
            },
            {
                'title': 'Basketball',
                'price': 3000.00,
                'original_price': 4000.00,
                'description': 'Official size basketball with excellent grip. Perfect for outdoor play.',
                'category': 'Sports',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=500&h=500&fit=crop',
            },
            # Baby & Kids
            {
                'title': 'Baby Stroller',
                'price': 25000.00,
                'original_price': 30000.00,
                'description': 'Lightweight foldable baby stroller. Easy to carry and store.',
                'category': 'Baby & Kids',
                'image_url': 'https://images.unsplash.com/photo-1555255705-5ad0b0e8b0e0?w=500&h=500&fit=crop',
            },
            {
                'title': 'Kids Bicycle',
                'price': 18000.00,
                'original_price': 22000.00,
                'description': 'Safe kids bicycle with training wheels. Perfect for learning to ride.',
                'category': 'Baby & Kids',
                'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&h=500&fit=crop',
            },
            # Men's Shirts
            {
                'title': 'Men\'s Casual Shirt',
                'price': 2500.00,
                'original_price': 3500.00,
                'description': 'Comfortable cotton casual shirt for men. Perfect for everyday wear. Available in multiple colors.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1594938291221-94f18e0a5726?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            },
            {
                'title': 'Men\'s Formal Shirt',
                'price': 3000.00,
                'original_price': 4000.00,
                'description': 'Premium formal shirt for men. Perfect for office and formal occasions. Wrinkle-free fabric.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1603252109303-2751441dd157?w=500&h=500&fit=crop',
            },
            {
                'title': 'Men\'s Polo Shirt',
                'price': 2200.00,
                'original_price': 3000.00,
                'description': 'Classic polo shirt for men. Comfortable and stylish. Perfect for casual outings.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop',
            },
            {
                'title': 'Men\'s Checkered Shirt',
                'price': 2800.00,
                'original_price': 3800.00,
                'description': 'Stylish checkered pattern shirt for men. Trendy and comfortable.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop',
            },
            {
                'title': 'Men\'s Denim Shirt',
                'price': 3200.00,
                'original_price': 4200.00,
                'description': 'Classic denim shirt for men. Durable and stylish. Perfect for casual wear.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop',
            },
            # Women's/Girly Shirts
            {
                'title': 'Women\'s Floral Shirt',
                'price': 2400.00,
                'original_price': 3400.00,
                'description': 'Beautiful floral print shirt for women. Feminine and elegant. Perfect for casual and semi-formal occasions.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop',
            },
            {
                'title': 'Women\'s Casual T-Shirt',
                'price': 1800.00,
                'original_price': 2500.00,
                'description': 'Comfortable cotton t-shirt for women. Soft fabric, perfect for everyday wear. Available in multiple colors.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500&h=500&fit=crop',
            },
            {
                'title': 'Women\'s Blouse',
                'price': 3500.00,
                'original_price': 4500.00,
                'description': 'Elegant blouse for women. Perfect for office and formal occasions. Premium quality fabric.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=500&h=500&fit=crop',
            },
            {
                'title': 'Women\'s Off-Shoulder Top',
                'price': 2800.00,
                'original_price': 3800.00,
                'description': 'Trendy off-shoulder top for women. Stylish and comfortable. Perfect for parties and casual outings.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop',
            },
            {
                'title': 'Women\'s Crop Top',
                'price': 2000.00,
                'original_price': 2800.00,
                'description': 'Fashionable crop top for women. Trendy and comfortable. Perfect for casual wear.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1617137968427-85924c800a22?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            },
            {
                'title': 'Women\'s Striped Shirt',
                'price': 2600.00,
                'original_price': 3600.00,
                'description': 'Classic striped shirt for women. Timeless design, perfect for any occasion.',
                'category': 'Fashion',
                'image_url': 'https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=500&h=500&fit=crop',
            },
        ]

        # Create products
        created_count = 0
        for data in products_data:
            product, created = Product.objects.get_or_create(
                title=data['title'],
                defaults={
                    'price': data['price'],
                    'original_price': data.get('original_price'),
                    'description': data['description'],
                    'category': data['category'],
                    'image_url': data.get('image_url', ''),
                    'sold_count': random.randint(10, 500),
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created: {product.title}')
                )
            else:
                # Update existing product with image_url if it doesn't have one
                if not product.image_url and data.get('image_url'):
                    product.image_url = data['image_url']
                    product.save()
                self.stdout.write(
                    self.style.WARNING(f'⚠ Already exists: {product.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Successfully created {created_count} new products with images!'
            )
        )
