from django.db import models
from django.utils.translation import gettext as _

from uuid import uuid4

class CartModel(models.Model):
    id = models.UUIDField(verbose_name=_('id_cart'),primary_key=True,default=uuid4,editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('shop.ProductModel', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]

    def get_item_total_price(self):
        return self.product.price * self.quantity