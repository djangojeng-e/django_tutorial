from django.db import models

# Create your models here.


from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name


class NewManager(models.Manager):
    # ...
    pass


class MyPerson(Person):
    objects = NewManager()
    # Meta 클래스 안에, Proxy = True  로 설정

    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

    def __str__(self):
        return self.last_name


class OrderedPerson(Person):
    class Meta:
        ordering = ['last_name']
        proxy = True

        def __str__(self):
            return self.last_name

