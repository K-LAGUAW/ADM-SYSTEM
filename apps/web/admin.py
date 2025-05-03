from .models import Customer
from django.contrib import admin

@admin.register(Customer)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'phone', 'province', 'locality')