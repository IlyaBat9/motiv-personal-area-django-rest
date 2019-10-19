from django.urls import path
from .views import GetBalance


urlpatterns = [
    path("", GetBalance.as_view())
]
