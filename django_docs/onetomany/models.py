from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    brand_name = models.CharField("제조사", max_length=30)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    car_model = models.CharField("자동차모델", max_length=40)

    def __str__(self):
        return self.car_model