from rest_framework import serializers

from shop.models import ProductModel
from .models import CartModel,CartItemModel

class AddCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ['id','product','quantity']
    def create(self, validated_data):
        cart_pk = self.context['cart_pk']
        product_pk = validated_data.get('product')
        quantity = validated_data.get('quantity')

        try:
            cart_item = CartItemModel.objects.get(cart_id=cart_pk,product_id=product_pk)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItemModel.DoesNotExist:
            cart_item = CartItemModel.objects.create(cart_id=cart_pk,**validated_data)
        self.instance = cart_item

        return cart_item

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ['quantity']
        read_only = ['product']
class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id','title','price']

class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(read_only=True)
    item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItemModel
        fields = ['id','cart','product','quantity','item_total_price']

    def get_item_total_price(self,item):
        return item.get_item_total_price()
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartModel
        fields = ['id','items','total_price']

    def get_total_price(self,cart):
        return sum( item.get_item_total_price() for item in cart.items.all())

