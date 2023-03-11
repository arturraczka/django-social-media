from apps.profiles.models import Profile
from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete = models.CASCADE, default = None)
    body = models.CharField(max_length = 1200, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user_profile}: "
            f"{self.created_at:%Y-%m-%d %H:%M}: "
            f"{self.body[:40]}..."
        )

