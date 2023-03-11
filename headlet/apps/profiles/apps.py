from django.apps import AppConfig
from django.core.signals import request_finished


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.profiles'

    def ready(self):
        import apps.signals

