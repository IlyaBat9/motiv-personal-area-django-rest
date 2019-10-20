from django.urls import path
from .views import GetTariffs


urlpatterns = [
    path("", GetTariffs.as_view())
]
