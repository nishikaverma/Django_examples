from django.db import models

class Grocry_Store(models.Model):
    Vegies=models.CharField(max_length=30)
    price_per_kg =models.FloatField()
