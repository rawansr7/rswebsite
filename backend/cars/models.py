from django.db import models
from user.models import User


class Car(models.Model):
    brand = models.CharField(max_length=500)
    year = models.IntegerField()
    price = models.IntegerField()
    stars = models.IntegerField()
    description = models.TextField()
    image_urls = models.JSONField()
    seats = models.IntegerField()
    bags = models.IntegerField()
    doors = models.IntegerField()


class Order(models.Model):
    LOCATIONS = [
        ("International Airport", "International Airport"),
        ("Delivery Service", "Delivery Service"),
        ("Our Main Office", "Our Main Office"),
    ]
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, blank=True, null=True, related_name="orders"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")

    return_date = models.DateTimeField()
    return_location = models.CharField(choices=LOCATIONS, max_length=50)
    pickup_date = models.DateTimeField()
    pickup_location = models.CharField(choices=LOCATIONS, max_length=50)

    ordered = models.BooleanField(default=False)


# class User(models.Model):
#     pass


# class Reservation(models.Model):
#     pass
