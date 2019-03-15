from django.contrib import admin
from .models import *


# Register your models here.
class AdsCategoryAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', ]
    search_fields = ['__unicode__']

    class Meta:
        model = Category


admin.site.register(Category, AdsCategoryAdmin)


class NewAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', ]
    search_fields = ['__unicode__']

    class Meta:
        model = News


admin.site.register(News, NewAdmin)
