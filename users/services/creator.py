from users.models import User
from app.errors import ObjectAlreadyExists


class UserCreator:
    def __init__(self, username, password):
        self.username = str(username).lower()
        self.password = password

    def __call__(self):
        if self.allowed_to_create():
            user = self.create()
            user.save()
            return user
        else:
            return None

    def create(self):
        return User.objects.create_user(
            email=self.username,
            password=self.password,
        )

    def allowed_to_create(self):
        if User.objects.filter(email=self.username).exists():
            raise ObjectAlreadyExists(
                f"User with username - {self.username} already exists"
            )

        return True
