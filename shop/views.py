from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductModel,ProductStatusType,CategoryModel 
from .serializers import ProductSerializer , CategorySerializer
from .filters import *
from .pagination import CustomProductPagination
from .permissions import IsAdminOrReadOnlyPermission

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