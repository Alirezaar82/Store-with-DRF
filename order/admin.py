from django.contrib import admin

from .models import *


@admin.register(OrderModel)
class AdminOrder(admin.ModelAdmin):
    pass

@admin.register(OrderItemModel)
class AdminOrderitem(admin.ModelAdmin):
    pass