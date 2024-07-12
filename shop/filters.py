from django_filters.rest_framework import FilterSet
from rest_framework.filters import SearchFilter

from .models import ProductModel


class ProductFilter(FilterSet):
    class Meta:
        model = ProductModel
        fields  = {
            'category' : ['exact'],
            'created_at' : ['gte', 'lte'],

        }


class CustomSearchFilter(SearchFilter):
    search_param = 'q'