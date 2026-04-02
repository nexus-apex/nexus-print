from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import PrintOrder, PrintProduct, PrintCustomer
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusPrint with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusprint.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if PrintOrder.objects.count() == 0:
            for i in range(10):
                PrintOrder.objects.create(
                    order_number=f"Sample {i+1}",
                    customer_name=f"Sample PrintOrder {i+1}",
                    product_type=random.choice(["business_cards", "banners", "brochures", "flyers", "stickers", "packaging"]),
                    quantity=random.randint(1, 100),
                    total=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["received", "designing", "printing", "ready", "delivered"]),
                    due_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 PrintOrder records created'))

        if PrintProduct.objects.count() == 0:
            for i in range(10):
                PrintProduct.objects.create(
                    name=f"Sample PrintProduct {i+1}",
                    category=random.choice(["cards", "large_format", "marketing", "packaging", "custom"]),
                    base_price=round(random.uniform(1000, 50000), 2),
                    min_quantity=random.randint(1, 100),
                    production_time_days=random.randint(1, 100),
                    status=random.choice(["active", "discontinued"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 PrintProduct records created'))

        if PrintCustomer.objects.count() == 0:
            for i in range(10):
                PrintCustomer.objects.create(
                    name=f"Sample PrintCustomer {i+1}",
                    company=["TechVision Pvt Ltd","Global Solutions","Pinnacle Systems","Nova Enterprises","CloudNine Solutions","MetaForge Inc","DataPulse Analytics","QuantumLeap Tech","SkyBridge Corp","Zenith Innovations"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    orders_count=random.randint(1, 100),
                    total_spent=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "inactive"]),
                    discount_rate=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 PrintCustomer records created'))
