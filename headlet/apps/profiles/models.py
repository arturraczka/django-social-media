from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, related_name = 'profile')
    about = models.TextField()
    avatar = models.ImageField(default = 'default.jpg', upload_to = 'profile_images')
    follows = models.ManyToManyField(
        'self',
        related_name = 'followed_by',
        symmetrical = False,
        blank = True,
    )
    profile_slug = models.SlugField(null=True)

    def __str__(self):
        return self.user.get_username()

    def save(self, *args, **kwargs):
        if not self.id:
            self.profile_slug = slugify(self.user.get_username())
        super(Profile, self).save(*args, **kwargs)