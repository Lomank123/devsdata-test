from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import MainLoginView, MainLogoutView
from main.urls import api_urlpatterns as main_api


api_urlpatterns = [
    path("event/", include(main_api), name="event-api"),
]


urlpatterns = [
    # Admin dashboard
    path("admin/", admin.site.urls),

    # Plain views
    path("", include("main.urls")),

    # API
    path("api/", include(api_urlpatterns)),

    # Auth
    path("login/", MainLoginView.as_view(), name="login"),
    path("logout/", MainLogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
