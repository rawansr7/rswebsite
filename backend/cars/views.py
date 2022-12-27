from django.shortcuts import redirect, render
from cars.models import Car


def flats_details(request, pk):
    car = Car.objects.get(pk=pk)
    return render(
        request,
        "sFlats.html",
        {"car": car},
    )


def all_flats(request):
    cars = Car.objects.all()
    return render(request, "Flats.html", {"cars": cars})


def reservation(request):
    return redirect("step1")


def step1(request):
    return render(request, "step1.html")


def step2(request):
    cars = Car.objects.all()
    return render(request, "step2.html", {"cars": cars})


def step3(request):
    car = Car.objects.get(pk=1)
    return render(
        request,
        "step3.html",
        {"car": car},
    )

def sstep3(request, pk):
    car = Car.objects.get(pk=pk)
    return render(
        request,
        "step3.html",
        {"car": car},
    )