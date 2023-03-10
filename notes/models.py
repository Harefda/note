from django.db import models


class Note(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="notes"
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.__str__()} {self.title} Wallet"
