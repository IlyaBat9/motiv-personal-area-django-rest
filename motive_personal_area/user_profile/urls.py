from django.urls import path
from .views import UserBaseInfoView, get_full_info

urlpatterns = [
    path(r"base/", UserBaseInfoView.as_view()),
    path(r"full/", get_full_info)
]
