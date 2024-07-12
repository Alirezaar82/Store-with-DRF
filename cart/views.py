from django.utils.translation import gettext as _

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status 

from cart.models import CartItemModel, CartModel

from .serializers import AddCartItemSerializer, CartItemSerializer, CartSerializer, UpdateCartItemSerializer


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartModel.objects.prefetch_related('items__product').all()
    def list(self, request, *args, **kwargs):
        return Response(_('nothing hier'),status=status.HTTP_401_UNAUTHORIZED)
    
class CartItemViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete','head','options']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_queryset(self):
        cart_pk = self.kwargs['cart_pk']
        queryset = CartItemModel.objects.select_related('product').filter(cart_id=cart_pk).all()
        return queryset
    
    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context['cart_pk'] = self.kwargs['cart_pk']
        return context
        
