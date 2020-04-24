from django.contrib import admin

# Register your models here.

from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['blog', 'headline', 'body_text',
                    'pub_date', 'mod_date', 'number_of_comments',
                    'number_of_pingbacks', 'rating']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)


