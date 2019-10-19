from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import UserBaseInfoSerializer
from .models import Profile


class UserBaseInfoView(generics.RetrieveAPIView):
    serializer_class = UserBaseInfoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

