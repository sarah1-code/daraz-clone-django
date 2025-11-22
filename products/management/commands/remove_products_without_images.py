from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Removes products that don\'t have images (neither image file nor image_url)'

    def handle(self, *args, **options):
        # Find products without images - check all combinations
        from django.db.models import Q
        
        # Get all products
        all_products = Product.objects.all()
        products_to_delete = []
        
        for product in all_products:
            has_image_file = product.image and product.image.name
            has_image_url = product.image_url and product.image_url.strip()
            
            # If product has neither image file nor image URL, mark for deletion
            if not has_image_file and not has_image_url:
                products_to_delete.append(product)
        
        count = len(products_to_delete)
        
        if count == 0:
            self.stdout.write(
                self.style.SUCCESS('All products have images. Nothing to delete!')
            )
            return
        
        # Show products that will be deleted
        self.stdout.write(
            self.style.WARNING(f'\nFound {count} product(s) without images:')
        )
        for product in products_to_delete:
            self.stdout.write(f'  - {product.title} (ID: {product.id}, Category: {product.category})')
        
        # Ask for confirmation
        self.stdout.write(
            self.style.WARNING('\nThese products will be PERMANENTLY deleted!')
        )
        
        # Delete products
        deleted_count = 0
        for product in products_to_delete:
            product_title = product.title
            product.delete()
            deleted_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Deleted: {product_title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully deleted {deleted_count} product(s) without images!'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Remaining products: {Product.objects.count()}'
            )
        )

