from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ("name", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("created_by", "prod_name", "in_stock", "price", "created")
    search_fields = ("prod_name", "created_by")
    list_display_links = ("created_by", "prod_name")
