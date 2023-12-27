from django.contrib import admin
from .models import Category, Product, Order, Customer, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","product" ,"created_at", "updated_at")
    search_fields = ("name",)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    
    display_categories.short_description = 'Categories'


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_date", "total_amount", "created_at", "updated_at")
    search_fields = ("order_date",)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "updated_at")
    search_fields = ("name",)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("rating", "comment", "product", "created_at", "updated_at")
    search_fields = ("product",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Review, ReviewAdmin)
