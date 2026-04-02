from django.db import models

class PrintOrder(models.Model):
    order_number = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255, blank=True, default="")
    product_type = models.CharField(max_length=50, choices=[("business_cards", "Business Cards"), ("banners", "Banners"), ("brochures", "Brochures"), ("flyers", "Flyers"), ("stickers", "Stickers"), ("packaging", "Packaging")], default="business_cards")
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("received", "Received"), ("designing", "Designing"), ("printing", "Printing"), ("ready", "Ready"), ("delivered", "Delivered")], default="received")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.order_number

class PrintProduct(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("cards", "Cards"), ("large_format", "Large Format"), ("marketing", "Marketing"), ("packaging", "Packaging"), ("custom", "Custom")], default="cards")
    base_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    min_quantity = models.IntegerField(default=0)
    production_time_days = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("discontinued", "Discontinued")], default="active")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class PrintCustomer(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    orders_count = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    discount_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
