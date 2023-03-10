from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from users.models import User


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created):
    if created:
        Token.objects.get_or_create(user=instance)
