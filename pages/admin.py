from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
     def Thumbnail(self, object):
          return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

     Thumbnail.short_description = 'imagem'

     list_display = ("Thumbnail", "first_name", "last_name", "designation", "created_date" )
     search_fields = ('first_name', 'designation')
     list_filter = ('designation',)