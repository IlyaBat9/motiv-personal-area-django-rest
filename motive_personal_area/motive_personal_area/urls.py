from django.contrib import admin
from django.urls import path, include


api_urlpatterns = [
    path(r"auth/", include("registration.urls"))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_urlpatterns)),
]
