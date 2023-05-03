from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from lotto.models import Lotto, Weekend
from lotto.serializers import LottoSerializer, WeekendSerializer
import pandas as pd

import requests
import json


def save_numbers_to_db(request):
    df = pd.read_excel('static/excel/lotto.xlsx')
    lotto_numbers = []
    numbers = []

    for index, row in df.iterrows():
        count = str(row["회차"])
        numbers.append(str(int(row["번호1"])) + " " + str(int(row["번호2"])) + " " + str(int(row["번호3"])) + " " + str(
            int(row["번호4"])) + " " + str(int(row["번호5"])) + " " + str(
            int(row["번호6"])) + " " + str(int(row["보너스"])))

    numbers.reverse()

    for number in range(0, len(numbers)):
        lotto_numbers.append(Lotto(count=number + 1, number=numbers[number]))

    Lotto.objects.bulk_create(lotto_numbers)
    return HttpResponse("Connection Successful!")


def load_weekend_number(request):
    count = Weekend.objects.latest('count')
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}".format(count)

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
    return HttpResponse("Connection Success!")


class LottoList(generics.ListAPIView):
    queryset = Lotto.objects.all()
    serializer_class = LottoSerializer


class WeekendLotto(generics.ListAPIView):
    queryset = Weekend.objects.all()
    serializer_class = WeekendSerializer
