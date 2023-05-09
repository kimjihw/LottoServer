import json
import logging
import time
import requests

from apscheduler.schedulers.background import BackgroundScheduler
from .models import Weekend, Lotto

logging.basicConfig(filename="apscheduler.log", level=logging.DEBUG)


def auto_check():

    latest_result = Weekend.objects.latest('count')
    count = int(latest_result.count) + 1
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(count)
    res = requests.get(url)
    json_data = json.loads(res.text)

    rst = []

    date = str(json_data["drwNoDate"])
    count = str(json_data['drwNo'])
    numbers = str(json_data["drwtNo1"]) + " " + str(json_data["drwtNo2"]) + " " + str(
        json_data["drwtNo3"]) + " " + str(
        json_data["drwtNo4"]) + " " + str(json_data["drwtNo5"]) + " " + str(json_data["drwtNo6"]) + " " + str(
        json_data["bnusNo"])

    rst.append(Weekend(date=date, count=count, numbers=numbers))

    Weekend.objects.create(date=date, count=count, numbers=numbers)

    Lotto.objects.create(count=count, number=numbers)

    print("Scheduler is alive!!")
    logging.info("Job executed")


scheduler = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')

scheduler.add_job(auto_check, 'cron', second=0, id='test')
logging.info("Scheduler started")
scheduler.start()

scheduler._thread.join()
