from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):

    list_display = ('id', 'url')
    list_display_links = ('id', 'url')
