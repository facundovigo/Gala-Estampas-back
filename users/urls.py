from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewset


router = DefaultRouter()
router.register(r'auth', CustomUserViewset, basename='auth')
urlpatterns = router.urls