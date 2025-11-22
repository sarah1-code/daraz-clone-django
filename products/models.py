from django.db import models
from django.db.models import Avg, Count

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="External image URL if no file uploaded")
    sold_count = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=100)
    
    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        """Calculate average rating from reviews"""
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0.0
    
    @property
    def review_count(self):
        """Get total number of reviews"""
        return self.reviews.count()
    
    @property
    def discount_percentage(self):
        """Calculate discount percentage if original_price exists"""
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return int(discount)
        return 0
