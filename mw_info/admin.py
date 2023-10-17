from django.contrib import admin


# Register your models here.
from .models import *


class MwAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'cat',)
    list_filter = ('time_create','cat')

class CategoriyaAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)


admin.site.register(MwInfo, MwAdmin)
admin.site.register(Category, CategoriyaAdmin)
