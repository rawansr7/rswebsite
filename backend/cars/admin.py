from django.contrib import admin
from .models import Car, Order


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
