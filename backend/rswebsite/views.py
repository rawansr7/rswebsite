from django.shortcuts import render
from cars.models import Car
from django.views.generic.base import TemplateView


def flats_details(request, pk):
    car = Car.objects.get(pk=pk)
    return render(
        request,
        "sFlats.html",
        {"car": car, "stars_iter": ["s"] * car.stars},
    )


class Flats(TemplateView):
    template_name = "Flats.html"
    cars = Car.objects.all()
    stars_iter = [["s"] * car.stars for car in cars]
    cars_and_stars = zip(cars, stars_iter)
    extra_context = {"cars_and_stars": cars_and_stars, "main_url": "sflats"}
