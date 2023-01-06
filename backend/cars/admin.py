from django.contrib import admin
from .models import Car, Order, CarDesign, Option, AddedOptionInfo


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]


@admin.register(CarDesign)
class CarDesignAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CarDesign._meta.fields]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Option._meta.fields]


@admin.register(AddedOptionInfo)
class AddedOptionInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddedOptionInfo._meta.fields]
