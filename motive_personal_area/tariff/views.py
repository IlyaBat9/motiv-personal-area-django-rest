from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import TariffSerializer
from .models import Tariff


class GetTariffs(generics.ListAPIView):
    serializer_class = TariffSerializer
    permission_classes = ()
    queryset = Tariff.objects.all()

    def get_object(self):
        return Tariff.objects.all()
