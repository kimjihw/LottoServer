import json
import logging

import requests

from lotto.models import Weekend, Lotto


def get_weekend():
    # latest_result = Weekend.objects.latest('count')
    # count = int(latest_result.count) + 1
    # url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(count)
    # res = requests.get(url)
    # json_data = json.loads(res.text)
    #
    # rst = []
    #
    # date = str(json_data["drwNoDate"])
    # count = str(json_data['drwNo'])
    # numbers = str(json_data["drwtNo1"]) + " " + str(json_data["drwtNo2"]) + " " + str(
    #     json_data["drwtNo3"]) + " " + str(
    #     json_data["drwtNo4"]) + " " + str(json_data["drwtNo5"]) + " " + str(json_data["drwtNo6"]) + " " + str(
    #     json_data["bnusNo"])
    #
    # rst.append(Weekend(date=date, count=count, numbers=numbers))
    #
    # Weekend.objects.create(date=date, count=count, numbers=numbers)
    #
    # Lotto.objects.create(count=count, number=numbers)
    logger = logging.getLogger('django')
    logger.info("Crontab is alive!!")
    print("Scheduler is alive!!")
