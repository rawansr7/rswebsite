from django.shortcuts import redirect, render
from cars.models import Car


def flats_details(request, pk):
    if request.method == "POST":
        # TODO: save it in db
        return redirect("step2", pk=pk)
    elif request.method == "GET":
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
    cars = Car.objects.all()
    return render(request, "step1.html", {"cars": cars})


def step2(request, pk):
    if request.method == "GET":
        return render(request, "step2.html")

    elif request.method == "POST":
        # do something
        return redirect("step3", pk=pk)


def step3(request, pk):
    car = Car.objects.get(pk=pk)
    return render(
        request,
        "step3.html",
        {"car": car},
    )
