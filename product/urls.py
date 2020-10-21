from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'supply', SupplyViewSet, basename='supply')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'client', ClientViewSet, basename='client')
router.register(r'zip_amount', ZipAmountViewSet, basename='ZipAmount')
urlpatterns = router.urls
