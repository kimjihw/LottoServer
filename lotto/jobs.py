import logging.config

from apscheduler.schedulers.background import BackgroundScheduler

from lotto import api

def job():
    api.get_weekend()


def scheduler_test():
    scheduler = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')

    scheduler.add_job(job, 'interval', seconds=10, id='scheduler_test')
    scheduler.start()

scheduler_test()