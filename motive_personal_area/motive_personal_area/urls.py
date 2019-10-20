from django.contrib import admin
from django.urls import path, include


api_urlpatterns = [
    path(r"auth/", include("registration.urls")),
    path(r"balance/", include("balance_info.urls")),
    path(r"tariffs/", include("tariff.urls")),
    path(r"base-info/", include("user_profile.urls")),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"api/", include(api_urlpatterns)),
]
