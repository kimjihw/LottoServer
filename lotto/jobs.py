import logging.config

from apscheduler.schedulers.background import BackgroundScheduler

from .api import get_weekend

def job():
    get_weekend()


def scheduler_test():
    scheduler = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')

    scheduler.add_job(job, 'cron', second=1, id='test')
    logging.info("Scheduler started")
    scheduler.start()

scheduler_test()