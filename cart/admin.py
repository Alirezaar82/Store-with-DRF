from django.contrib import admin

from .models import CartModel,CartItemModel


@admin.register(CartModel)
class AdminCart(admin.ModelAdmin):
    pass

@admin.register(CartItemModel)
class AdminCartItem(admin.ModelAdmin):
    pass