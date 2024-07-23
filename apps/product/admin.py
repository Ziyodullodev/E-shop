from django.contrib import admin
from apps.product.models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at", "updated_at"]
    search_fields = ["title", "description"]
    list_filter = ["created_at", "updated_at"]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "price",
        "category",
        "created_at",
        "updated_at",
    ]
    search_fields = ["title", "description"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
