from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet


router = DefaultRouter()
router.register(r'events', PedidoViewSet, basename='events')
urlpatterns = router.urls