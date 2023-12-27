from django.forms import ModelForm
from django import forms
from myapp.models import Category,Customer,Order,Product,Review

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderForm(ModelForm):   
    class Meta:
        model = Order
        fields = "__all__"
        
class ProductForm(ModelForm): 
    class Meta:
        model =Product
        fields = "__all__"
        
class ReviewForm(ModelForm):   
    class Meta:
        model = Review
        fields = "__all__"