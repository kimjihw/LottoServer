from django.db import models

# Create your models here.
class Lotto(models.Model):
    count = models.CharField(max_length=10000)
    number = models.CharField(max_length=10000)

    def __str__(self):
        return f"LottoNumbers for {self.count}"
