from django.contrib import admin
from .models import Team

# Register your models here.
@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
     list_display = ("first_name", "last_name", "designation" )