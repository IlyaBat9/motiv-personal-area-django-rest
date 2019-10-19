from django.urls import path
from .views import login, change_password


urlpatterns = [
    path("login/", login),
    path("change-password/", change_password)
]
