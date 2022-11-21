from django.contrib import admin

# Register your models here.
from .models import Team

# Register your models here.
@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
     list_display = ("first_name", "last_name", "designation" )