from django.db import models

# Create your models here.
# 각각의 모델을 수정 혹은 추가할때마다
# python mangae.py makemigrations
# python manage.py migrate


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name + " " + self.shirt_size


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

    def __str__(self):
        return self.name + " " + self.medal


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


# 각각의 모델을 수정 혹은 추가할때마다
# python mangae.py makemigrations
# python manage.py migrate