from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('pedidos.urls')),
    path('', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Administración Gala Estampas'