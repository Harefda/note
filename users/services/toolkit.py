from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from app.errors import ValidationError
from users.models import User
from users.services.creator import UserCreator


class UserToolKit:
    @classmethod
    def create_user(cls, username, password):
        return UserCreator(password=password, username=username)()

    @classmethod
    def authenticate_user(cls, email, password):
        user = authenticate(email=email, password=password)
        if not user:
            qs = User.objects.filter(email=email)
            if qs.exists() and not qs.first().is_active:
                raise ValidationError("Account is not active")
            raise ValidationError("Wrong email or password")

        return user, Token.objects.get_or_create(user=user)[0]
