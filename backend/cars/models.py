from django.db import models


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


# class User(models.Model):
#     pass


# class Reservation(models.Model):
#     pass
