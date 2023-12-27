# myapp/create_initial_data.py
import random
from faker import Faker
from django.db import IntegrityError
from myapp.models import Category, Product, Order, Customer, Review
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

fake = Faker()

class Command(BaseCommand):
    help = 'Create initial data for the myapp models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))

        # Create categories
        create_categories()

        # Create products
        create_products()

        # Create customers
        create_customers()

        # Create orders
        create_orders()

        # Create reviews
        create_reviews()

        self.stdout.write(self.style.SUCCESS('Initial data creation complete.'))

def create_categories():
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Toys']
    for category_name in categories:
        Category.objects.get_or_create(name=category_name)

def create_products(num_products=20):
    categories = Category.objects.all()
    for _ in range(num_products):
        Product.objects.get_or_create(
            name=fake.company(),  # Use company() for product names
            description=fake.text(),
            image='product_images/default_product.jpg',
            price=random.uniform(10, 1000),
            category=random.choice(categories),
        )

def create_orders(num_orders=10, max_products_per_order=5):
    products = Product.objects.all()
    customers = Customer.objects.all()
    for _ in range(num_orders):
        order = Order.objects.create(
            order_date=fake.date_between('-1y', 'today'),
            total_amount=0
        )

        selected_products = random.sample(list(products), k=random.randint(1, max_products_per_order))
        for product in selected_products:
            order.products.add(product)
            order.total_amount += product.price

        order.save()

        # Assign orders to random customers
        random_customer = random.choice(customers)
        random_customer.orders.add(order)  # Use orders field to associate orders with customers

def create_customers(num_customers=15):
    for _ in range(num_customers):
        email = fake.email()
        try:
            customer = Customer.objects.create(
                name=fake.name(),
                email=email,
            )

            # Optionally, you can associate random orders with customers here if needed.
            # For example:
            # create_orders(num_orders=random.randint(1, 5), max_products_per_order=3)
        except IntegrityError:
            # If the email already exists, generate a new one
            continue
def create_reviews(num_reviews=50):
    products = Product.objects.all()
    for _ in range(num_reviews):
        Review.objects.create(
            rating=random.randint(1, 5),
            comment=fake.text(),
            product=random.choice(products),
        )
