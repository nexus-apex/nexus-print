from django.contrib import admin
from .models import PrintOrder, PrintProduct, PrintCustomer

@admin.register(PrintOrder)
class PrintOrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "customer_name", "product_type", "quantity", "total", "created_at"]
    list_filter = ["product_type", "status"]
    search_fields = ["order_number", "customer_name"]

@admin.register(PrintProduct)
class PrintProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "base_price", "min_quantity", "production_time_days", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name"]

@admin.register(PrintCustomer)
class PrintCustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "email", "phone", "orders_count", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "company", "email"]
