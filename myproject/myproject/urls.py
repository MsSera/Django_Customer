from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import (
    HomePageView,
    CategoryListView,CategoryDeleteView,CategoryUpdateView,CategoryCreateView,
    ProductListView,ProductCreateView,ProductUpdateView,ProductDeleteView,
    OrderListView,OrderCreateView,OrderUpdateView,OrderDeleteView,
    CustomerListView,CustomerCreateView, CustomerUpdateView,CustomerDeleteView,
    ReviewListView,ReviewCreateView,ReviewUpdateView,ReviewDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/add/', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<int:pk>/',CategoryUpdateView.as_view(), name='category-edit'),
    path('category_list/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    
    path('product/', ProductListView.as_view(), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('product_list/<int:pk>/', ProductUpdateView.as_view(), name='product-edit'),
    path('product_list/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/add/', OrderCreateView.as_view(), name='order-add'),
    path('product_list/<int:pk>/', OrderUpdateView.as_view(), name='order-edit'),
    path('product_list/<int:pk>/delete', OrderDeleteView.as_view(), name='order-delete'),
    
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer-add'),
    path('customer_list/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer-edit'),
    path('customer_list/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/add/', ReviewCreateView.as_view(), name='review-add'),
    path('review_list/<int:pk>', ReviewUpdateView.as_view(), name='review-edit'),
    path('review_list/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
