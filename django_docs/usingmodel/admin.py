from django.contrib import admin

# Register your models here.

from .models import Person, Runner


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'shirt_size']
    list_display = ('name', 'shirt_size')


class RunnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'medal']


admin.site.register(Person, PersonAdmin)
admin.site.register(Runner, RunnerAdmin)