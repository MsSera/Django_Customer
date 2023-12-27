from django.shortcuts import render
from .models import Category, Product, Order, Customer, Review
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ProductForm, CategoryForm, OrderForm, CustomerForm, ReviewForm


class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 4

    def get_queryset(self):
        return Category.objects.all().prefetch_related('product')  # Use the correct related name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_crud\category_add.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_crud\category_edit.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_crud\category_del.html'
    success_url = reverse_lazy('category-list')
 
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products_crud\product_add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products_crud\product_edit.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products_crud\product_del.html'
    success_url = reverse_lazy('product-list')
    
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 3

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_crud\order_add.html'
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_crud\order_edit.html'
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_crud\order_del.html'
    success_url = reverse_lazy('order-list')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    paginate_by = 5

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_crud\customer_add.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_crud\customer_edit.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_crud\customer_del.html'
    success_url = reverse_lazy('customer-list')

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    paginate_by = 5

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_crud\\review_add.html'
    success_url = reverse_lazy('review-list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_crud\\review_edit.html'
    success_url = reverse_lazy('review-list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_crud\\review_del.html'
    success_url = reverse_lazy('review-list')
    
def my_view(request):
    product_cards = Product.objects.all()

    # Print image URLs for debugging
    for card in product_cards:
        print(f"{card.name}: {card.image}")

    return render(request, 'product_list.html', {'product_cards': product_cards})   
    