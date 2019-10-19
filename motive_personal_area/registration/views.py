from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import LoginSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(username=serializer.data.get("login"),
                        password=serializer.data.get("password"))
    if user is None:
        return Response({"detail": "Логин или пароль введены неверно"}, status=401)

    try:
        token = Token.objects.get(user=user)
    except ObjectDoesNotExist:
        return Response({"detail": "There is user that incorrect created"}, status=500)

    return Response(
        {"detail": "Login successful", "token": token.key}
    )
