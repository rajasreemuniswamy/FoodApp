from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    food_item = models.CharField(max_length=100)
    price = models.IntegerField()
    is_delivered=models.BooleanField()
    