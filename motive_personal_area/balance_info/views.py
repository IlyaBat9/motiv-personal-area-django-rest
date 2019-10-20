from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import BalanceSerializer
from .models import Balance


class GetBalance(generics.RetrieveAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Balance.objects.all

    def get_object(self):
        return Balance.objects.get(user=self.request.user)
