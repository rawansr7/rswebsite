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
    return render(request, "Flats.html", {"cars": cars})
