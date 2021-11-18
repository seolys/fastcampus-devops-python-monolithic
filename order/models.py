from django.db import models

# Create your models here.
class Shop(models.Model):
  shop_name = models.CharField(max_length=20)
  shop_address = models.CharField(max_length=40)

class Menu(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)

class Order(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  order_date = models.DateTimeField('date ordered') # 주문시간
  address = models.CharField(max_length=40)
  estimated_time = models.IntegerField(default=-1) # 예상시간
  deliver_finish = models.IntegerField(default=0) # 배달완료여부

class Orderfood(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)
