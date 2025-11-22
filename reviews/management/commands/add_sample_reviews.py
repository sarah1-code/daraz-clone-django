from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Product
from reviews.models import Review
import random

class Command(BaseCommand):
    help = 'Adds 10 sample reviews for each product'

    def handle(self, *args, **options):
        products = Product.objects.all()
        
        if not products.exists():
            self.stdout.write(
                self.style.ERROR('No products found. Please create products first.')
            )
            return

        # Sample review comments
        review_comments = [
            "Great product! Very satisfied with the quality.",
            "Excellent value for money. Highly recommended!",
            "Good product but delivery took longer than expected.",
            "Amazing quality! Exceeded my expectations.",
            "Product is okay, nothing special but works fine.",
            "Very happy with this purchase. Will buy again!",
            "Good product at a reasonable price.",
            "Fast delivery and product is as described.",
            "Quality is good but could be better.",
            "Perfect! Exactly what I was looking for.",
            "Not bad, but there are better options available.",
            "Great product, very satisfied!",
            "Good quality and fast shipping.",
            "Product arrived damaged but seller replaced it quickly.",
            "Excellent product, highly recommend!",
            "Good value for money.",
            "Product is fine but packaging could be better.",
            "Very happy with my purchase!",
            "Good product, meets expectations.",
            "Amazing quality! Worth every penny.",
        ]

        total_reviews = 0
        
        for product in products:
            # Get or create some test users for reviews
            users = list(User.objects.all())
            
            # If not enough users, create some
            while len(users) < 10:
                username = f"reviewer_{random.randint(1000, 9999)}"
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(
                        username=username,
                        email=f"{username}@example.com",
                        password='testpass123'
                    )
                    users.append(user)
            
            # Create 10 reviews for this product
            created_count = 0
            for i in range(10):
                user = random.choice(users)
                rating = random.choice([4, 5])  # Mostly positive reviews
                if random.random() < 0.2:  # 20% chance of lower rating
                    rating = random.choice([1, 2, 3])
                
                comment = random.choice(review_comments)
                
                # Check if this user already reviewed this product
                if not Review.objects.filter(user=user, product=product).exists():
                    Review.objects.create(
                        user=user,
                        product=product,
                        rating=rating,
                        comment=comment
                    )
                    created_count += 1
                    total_reviews += 1

            # Update product sold_count (random number between 10-100)
            if product.sold_count == 0:
                product.sold_count = random.randint(10, 100)
                product.save()

            self.stdout.write(
                self.style.SUCCESS(f'✓ Added {created_count} reviews for: {product.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Successfully created {total_reviews} reviews across {products.count()} products!'
            )
        )

