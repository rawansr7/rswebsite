from django.shortcuts import render
from cars.models import Car


def flats_details(request, pk):
    car = Car.objects.get(pk=pk)
    return render(
        request,
        "sFlats.html",
        {"car": car, "stars_iter": ["s"] * car.stars},
    )


def all_flats(request):
    cars = Car.objects.all()
    stars_iter = [["s"] * car.stars for car in cars]
    cars_and_stars = zip(cars, stars_iter)

    return render(
        request,
        "Flats.html",
        {"cars_and_stars": cars_and_stars, "main_url": "sflats"},
    )
