from django.db import models


# Create your models here.
class Lotto(models.Model):
    count = models.CharField(max_length=10000)
    number = models.CharField(max_length=10000)

    def __str__(self):
        return f"LottoNumbers for {self.count}"


class Weekend(models.Model):
    date = models.CharField(max_length=20)
    count = models.CharField(max_length=128)
    numbers = models.CharField(max_length=128)

    def __str__(self):
        return f"LottoNumbers for {self.count}"