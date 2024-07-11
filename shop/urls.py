from django.urls import path,include

from rest_framework_nested.routers import NestedDefaultRouter,DefaultRouter

from .views import CommentViewSet, ProductViewSet,CategoryViewSet

router = DefaultRouter()
router.register('products',ProductViewSet,basename='product')
router.register('categories',CategoryViewSet,basename='category')

product_comment_router = NestedDefaultRouter(router,'products',lookup='product')
product_comment_router.register('comments',CommentViewSet,basename='product_comment')

URLS = router.urls + product_comment_router.urls

urlpatterns = [
    path('',include(URLS))
]
