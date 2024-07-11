from django.urls import path,include

from rest_framework_nested.routers import NestedDefaultRouter,DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()
router.register('products',ProductViewSet,basename='product')
# router.register('products',ProductViewSet,basename='product')

urlpatterns = [
    path('',include(router.urls))
]
