from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import MainLoginView, MainLogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("event/", include("main.urls")),
    path("login/", MainLoginView.as_view(), name="login"),
    path("logout/", MainLogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
