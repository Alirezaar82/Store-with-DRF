from django.contrib import admin

from .models import CategoryModel,ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'created_at',
    ]

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'category',
        'price',
        'created_at',
    ]