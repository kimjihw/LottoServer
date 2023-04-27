from django.urls import path

from lotto.views import LottoList, save_numbers_to_db

urlpatterns = [
    path('lotto-list', LottoList.as_view()),
    path('save', save_numbers_to_db)
]
