from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# 새로운 서브 클래스 추가
class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')


