import logging.config

from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import BaseCommand

from lotto import api

class Command(BaseCommand):
    help = "Get weekend Lotto Numbers"

    def handle(self, *args, **options):
        api.get_weekend()