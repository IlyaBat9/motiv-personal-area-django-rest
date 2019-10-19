from django.urls import path
from .views import UserBaseInfoView

urlpatterns = [
    path(r"", UserBaseInfoView.as_view()),
]
