from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import UserBaseInfoSerializer
from .models import Profile
from balance_info.models import Balance
from balance_info.serializer import BalanceSerializer
from tariff.serializer import TariffSerializer
from tariff.models import Tariff


class UserBaseInfoView(generics.RetrieveAPIView):
    serializer_class = UserBaseInfoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_full_info(request):
    balance = Balance.objects.get(user=request.user)
    balance_serializer = BalanceSerializer(balance)
    base_serializer = UserBaseInfoSerializer(Profile.objects.get(user=request.user))
    tariff = Tariff.objects.last()
    tariff_serializer = TariffSerializer(tariff)
    return Response({"balance": balance_serializer.data,
                     "base": base_serializer.data,
                     "tariff": tariff_serializer.data})
