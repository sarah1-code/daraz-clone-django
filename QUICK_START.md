# 🚀 Quick Start: Add Products in 2 Steps

## ✅ Method 1: Automatic (Fastest - Recommended)

### Step 1: Run the command
```bash
python manage.py add_sample_products
```

### Step 2: Done! 
✅ 10 sample products are now in your database!

**Note:** Products are created without images. Add images later through Django Admin if needed.

---

## ✅ Method 2: Manual (Using Admin Panel)

### Step 1: Create Superuser
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### Step 2: Add Products
1. Start server: `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with your superuser credentials
4. Click "Products" → "Add Product"
5. Fill in product details and upload image
6. Click "Save"

---

## 🎯 Which Method to Choose?

- **Method 1**: Quick setup, get started immediately
- **Method 2**: Full control, add custom products with images

**Recommendation:** Use Method 1 first to test your site, then use Method 2 to add real products!

