from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Imagem'
    list_display = ('thumbnail', 'car_title', 'color', 'model', 'year', 'fuel_type', 'is_featured')
    list_filter = ('car_title', 'year')
    search_fields = ('car_title', 'vin_no')
    list_editable = ('is_featured',)