from django.urls import path

from users.views import *


urlpatterns = [
    path("create", create_user_api),
    path("authenticate", authenticate_user_api),
]
