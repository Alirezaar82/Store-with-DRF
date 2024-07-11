from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import CommentModel, CommentStatusType, ProductModel,ProductStatusType,CategoryModel 
from .serializers import CommentSerializer, ProductSerializer , CategorySerializer
from .filters import *
from .pagination import CustomProductPagination
from .permissions import IsAdminOrReadOnlyOrCreatePermission, IsAdminOrReadOnlyPermission

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.select_related('category').filter(status=ProductStatusType.published.value).all()
    filter_backends = [CustomSearchFilter,DjangoFilterBackend, OrderingFilter,]
    filterset_class = ProductFilter
    search_fields = ['title',]
    pagination_class = CustomProductPagination
    permission_classes = [IsAdminOrReadOnlyPermission]

    # def delete(self, request,pk):
    #     product = get_object_or_404(ProductModel,pk=pk)
    #     if product.order_items.count() > 0:
    #         return Response({_('error'):_('There is some order items relateing this product!!')})
    
    #     product.delete()
    #     return Response(_('product has delete'),status=status.HTTP_200_OK)
    

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    filter_backends = [CustomSearchFilter,DjangoFilterBackend, OrderingFilter,]
    permission_classes = [IsAdminOrReadOnlyPermission]

    # def delete(self, request,pk):
    #     product = get_object_or_404(ProductModel,pk=pk)
    #     if CategoryModel.product_category.count() > 0:
    #         return Response({_('error'):_('There is some order items relateing this category!!')})
    
    #     product.delete()
    #     return Response(_('category has delete'),status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnlyOrCreatePermission]

    def get_queryset(self):
        product_pk = self.kwargs['product_pk']
        if self.request.user.is_authenticated and self.request.user.is_staff:
            queryset = CommentModel.objects.filter(product_id=product_pk).all()
        else :
            queryset = CommentModel.objects.filter(product_id=product_pk,status=CommentStatusType.approved.value).all()
        return queryset
    
    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context['product_pk'] = self.kwargs['product_pk']
        return context
    
