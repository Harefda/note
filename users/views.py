import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.utils import get_body_data
from users.serializers import UserSerializer
from users.services.toolkit import UserToolKit


@api_view(["POST"])
def create_user_api(request):
    data = get_body_data(request, ["username", "password"])
    user = UserToolKit.create_user(data["username"], data["password"])
    serializer = UserSerializer(instance=user)
    return Response(serializer.data, status=201)


@api_view(["POST"])
def authenticate_user_api(request):
    data = get_body_data(request, ["username", "password"])
    user, token = UserToolKit.authenticate_user(data["username"], data["password"])
    serializer = UserSerializer(instance=user)
    return Response({"user": serializer.data, "token": str(token)}, status=200)
