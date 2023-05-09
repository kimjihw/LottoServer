from django.apps import AppConfig
from django.conf import settings


class LottoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lotto'

    def ready(self):
        from .jobs import scheduler_test
        from .models import Weekend, Lotto
        scheduler_test()
