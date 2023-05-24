from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name', 'slug')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'title', 'author', 'in_stock', 'price', 'created')
    prepopulated_fields  = {'slug': ('title',)}
    search_fields = ('title', 'created_by')
    list_display_links = ('created_by', 'title')