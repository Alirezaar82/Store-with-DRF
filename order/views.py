from django.db.models import Prefetch

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from .serializers import *

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete','head','options']

    def get_permissions(self):
        if self.request.method in  ['PATCH','DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        if self.request.user.is_staff:
            return AdminOrderSerializer
        return OrderSerializer
    
    def create(self, request, *args, **kwargs):
        order_create_serializer = OrderCreateSerializer(data=request.data,context=self.get_serializer_context())
        order_create_serializer.is_valid(raise_exception=True)
        order_create = order_create_serializer.save()
        serializers = OrderSerializer(order_create)
        return Response(serializers.data)
    
    def get_queryset(self):
        queryset = OrderModel.objects.select_related('customer__user_profile').prefetch_related( Prefetch(
                'items',
                OrderItemModel.objects.select_related('product'),
            )).all()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(customer_id=self.request.user.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user.id
        return context