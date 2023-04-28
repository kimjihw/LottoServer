import json

import requests
from crontab import CronTab

from lotto.models import Weekend


def renewer_weekend():
    count = 1064
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(count)
    res = requests.get(url)
    json_data = json.loads(res.text)

    rst = []

    date = str(json_data["drwNoDate"])
    count = str(json_data['drwNo'])
    numbers = str(json_data["drwtNo1"]) + " " + str(json_data["drwtNo2"]) + " " + str(json_data["drwtNo3"]) + " " + str(
        json_data["drwtNo4"]) + " " + str(json_data["drwtNo5"]) + " " + str(json_data["drwtNo6"]) + " " + str(
        json_data["bnusNo"])

    rst.append(Weekend(date=date, count=count, numbers=numbers))

    Weekend.objects.bulk_create(rst)
