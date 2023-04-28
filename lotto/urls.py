from django.urls import path

from lotto.views import LottoList, save_numbers_to_db, load_weekend_number

urlpatterns = [
    path('lotto-list', LottoList.as_view()),
    path('save', save_numbers_to_db),
    path('this-week', load_weekend_number)
]
