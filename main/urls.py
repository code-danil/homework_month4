from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars_of_facts.urls')),
    path('shop/', include('myShop.urls')),
    path('drivers/', include('drivers.urls')),
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
