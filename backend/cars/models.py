from django.db import models
from user.models import User


class Car(models.Model):
    brand = models.CharField(max_length=500)
    year = models.IntegerField()
    price = models.FloatField()
    stars = models.IntegerField()
    description = models.TextField()
    seats = models.IntegerField()
    bags = models.IntegerField()
    doors = models.IntegerField()
    insurance = models.FloatField()

    @property
    def available(self):
        designs = [design for design in self.designs.all() if design.available]
        return len(designs) > 0

    @property
    def default_design(self):
        available_designs = [
            design for design in self.designs.all() if design.available
        ]
        if len(available_designs):
            return available_designs[0]
        return self.designs.first()

    def __str__(self):
        return self.brand


class CarDesign(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="designs")
    image_url = models.CharField(max_length=500)

    @property
    def available(self):
        orders = self.orders.filter(status="ORDERED")
        return not orders.exists()


class Option(models.Model):
    TYPES = [("Protection", "Protection"), ("Additional", "Additional")]

    typ = models.CharField(choices=TYPES, max_length=50)
    title = models.CharField(max_length=500)
    description = models.TextField()
    image_url = models.CharField(max_length=500)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Order(models.Model):
    LOCATIONS = [
        ("International Airport", "International Airport"),
        ("Delivery Service", "Delivery Service"),
        ("Our Main Office", "Our Main Office"),
    ]
    STATUS = [
        ("PENDING", "PENDING"),
        ("ORDERED", "ORDERED"),
        ("COMPLETE", "COMPLETE"),
        ("CANCELLED", "CANCELLED"),
    ]
    car_design = models.ForeignKey(
        CarDesign, on_delete=models.CASCADE, related_name="orders"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")

    return_datetime = models.DateTimeField(blank=True, null=True)
    return_location = models.CharField(
        blank=True, null=True, choices=LOCATIONS, max_length=50
    )
    pickup_datetime = models.DateTimeField(blank=True, null=True)
    pickup_location = models.CharField(
        blank=True, null=True, choices=LOCATIONS, max_length=50
    )

    options = models.ManyToManyField(
        Option, through="AddedOptionInfo", blank=True, related_name="orders"
    )
    status = models.CharField(default="PENDING", choices=STATUS, max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cost(self):
        added_options = self.added_options_info.all()
        return self.car_design.car.price + sum(
            [
                added_option.option.price * added_option.count
                for added_option in added_options
            ]
        )

    class Meta:
        ordering = ["-created_at"]


class AddedOptionInfo(models.Model):
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name="added_options_info"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="added_options_info"
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.option.title} x {self.count}"
