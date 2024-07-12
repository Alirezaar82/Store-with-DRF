from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

USER = get_user_model()

class OrderStatustype(models.IntegerChoices):
    paid = 1,_('paid')
    unpaid = 2,_('unpaid')
    canceled = 3,_('canceled')

class OrderModel(models.Model):
    customer = models.ForeignKey(USER,on_delete=models.PROTECT,verbose_name=_('order_customer'))
    status = models.IntegerField(choices=OrderStatustype.choices,default=OrderStatustype.unpaid.value,verbose_name=_('status'))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)

class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.PROTECT, related_name='items',verbose_name=_('item_order'))
    product = models.ForeignKey('shop.ProductModel', on_delete=models.PROTECT, related_name='order_items_product')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        unique_together = [['order', 'product']]

    def __str__(self):
        return str(self.order)
    def get_item_total_price(self):
        
        return self.product.price * self.quantity
