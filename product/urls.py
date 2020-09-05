from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ProductViewSet, ArticleViewSet


router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'article', ArticleViewSet, basename='article')
urlpatterns = router.urls
