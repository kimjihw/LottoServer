from django.apps import AppConfig
from django.conf import settings


class LottoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lotto'

    def ready(self):
        if getattr(settings, 'SCHEDULER_DEFAULT', False):
            from . import jobs
            jobs.scheduler_test()
