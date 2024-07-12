from django.urls import path,include

from rest_framework_nested.routers import NestedDefaultRouter,DefaultRouter

from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('carts',CartViewSet,basename='cart')

cart_items_router = NestedDefaultRouter(router,'carts',lookup='cart')
cart_items_router.register('items',CartItemViewSet,basename='cart-item')
 

URLS = router.urls + cart_items_router.urls
urlpatterns = [
    path('',include(URLS)),
]
