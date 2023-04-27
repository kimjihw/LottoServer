from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from lotto.models import Lotto
from lotto.serializers import LottoSerializer
import pandas as pd


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


class LottoList(generics.ListAPIView):
    queryset = Lotto.objects.all()
    serializer_class = LottoSerializer
