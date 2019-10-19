from django.urls import path
from .views import login, change_password, login_otp


urlpatterns = [
    path("login/", login),
    path("otp-login/", login_otp),
    path("change-password/", change_password)
]
