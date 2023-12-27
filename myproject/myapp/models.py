# myapp/models.py
from django.db import models
import os
import uuid

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
def get_unique_filename(instance, filename):
    """Generate a unique filename for each uploaded file."""
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return os.path.join('product_images/', unique_filename)
class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image=models.ImageField(upload_to='product_images/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='products_related')

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, default=1, related_name='category_related')  # Add related_name here

    def __str__(self):
        return self.name
    
class Order(BaseModel):
    order_date = models.DateField()
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"

class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.name

class Review(BaseModel):
    rating = models.IntegerField()
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.product.name}"
