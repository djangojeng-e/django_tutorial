from django.contrib import admin

# Register your models here.

from .models import Car, Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    pass


class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'car_model')


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)