from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.prod_name

class Orders(models.Model):
    prod_name = models.CharField(max_length=100)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_id')
    buy_quantity = models.IntegerField()

    def __str__(self) -> str:
        return (f'{self.prod_name}')