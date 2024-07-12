from django.urls import path,include

from rest_framework_nested.routers import NestedDefaultRouter,DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register('orders',OrderViewSet,basename='order')

URLS = router.urls
urlpatterns = [
    path('',include(URLS)),
]
