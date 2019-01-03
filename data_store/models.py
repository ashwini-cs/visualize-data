from django.db import models

class MaxTemp(models.Model):
    region = models.CharField(max_length=20);
    year = models.IntegerField();
    month = models.CharField(max_length=10);
    max_temp = models.DecimalField(max_digits=4, decimal_places=2);

