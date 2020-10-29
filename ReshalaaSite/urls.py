
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('2/', include('Orders.urls')),
    path('', include('db_manager.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
