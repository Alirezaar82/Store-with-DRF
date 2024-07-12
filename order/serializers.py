from django.db import transaction


from rest_framework import serializers

from accounts.models import CustomUser
from cart.models import CartItemModel, CartModel
from shop.models import ProductModel
from .models import OrderItemModel,OrderModel

class OrderUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id','full_name',]

    def get_full_name(self,user):
        return user.user_profile.get_fullname()

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id','title','price']
        read_only_fields = ['product']

class OrderItemsSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(read_only=True)
    class Meta:
        model = OrderItemModel
        fields = ['id','product','quantity','price']

class AdminOrderSerializer(serializers.ModelSerializer):
    customer = OrderUserSerializer(read_only=True)
    items = OrderItemsSerializer(read_only=True,many=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = ['id','customer','items','status','created_at','total_price']
    def get_total_price(self,order):
        return sum( item.get_item_total_price() for item in order.items.all())

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(read_only=True,many=True)
    customer = OrderUserSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = ['id','customer','items','status','total_price']

    def get_total_price(self,order):
        return sum( item.get_item_total_price() for item in order.items.all())

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['status']

class OrderCreateSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        try:
            if CartModel.objects.get(id=cart_id).items.count() == 0 :
                raise serializers.ValidationError('your Cart is empty')
        except CartModel.DoesNotExist:
            raise serializers.ValidationError('Cart does not exist')
        return cart_id
        
    def save(self,**kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            user_id = self.context['user_id']

            cart_items = CartItemModel.objects.select_related('product').filter(cart_id=cart_id).all()
            customer = CustomUser.objects.get(id=user_id)

            order = OrderModel.objects.create(
                customer = customer,
            )
            
            for item in cart_items:
                OrderItemModel.objects.create(
                    order = order,
                    product_id = item.product_id,
                    quantity = item.quantity,
                    price = item.product.price
                )
            CartModel.objects.get(id=cart_id).delete()
            return order