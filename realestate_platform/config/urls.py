from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from properties import views as properties_views

urlpatterns = [
    path("", properties_views.home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("properties/", include("properties.urls")),
    path("chat/", include("chat.urls")),
    path("payments/", include("payments.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
