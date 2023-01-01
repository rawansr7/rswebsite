import datetime
from django.shortcuts import redirect, render
from cars.models import Car, Option, Order, AddedOptionInfo
from django.contrib.auth.decorators import login_required


def flats_details(request, pk):
    if request.method == "POST":
        car = Car.objects.get(pk=pk)
        order = Order(car=car, user=request.user)
        order.save()
        return redirect("step2", pk=order.id)
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


@login_required
def reservation(request):
    return redirect("step1")


@login_required
def step1(request):
    cars = Car.objects.all()
    return render(request, "step1.html", {"cars": cars})


@login_required
def step2(request, pk):
    if request.method == "GET":
        return render(request, "step2.html")

    elif request.method == "POST":
        pickup_location = request.POST.get("pickup_location")
        return_location = request.POST.get("return_location")
        pickup_datetime = request.POST.get("pickup_datetime")
        return_datetime = request.POST.get("return_datetime")
        order = Order.objects.get(pk=pk)
        order.pickup_location = pickup_location
        order.return_location = return_location
        order.pickup_datetime = datetime.datetime.strptime(
            pickup_datetime, "%Y-%m-%d %H:%M"
        )
        order.return_datetime = datetime.datetime.strptime(
            return_datetime, "%Y-%m-%d %H:%M"
        )
        order.save()

        return redirect("step3", pk=pk)


@login_required
def step3(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "GET":
        protection_options = Option.objects.filter(typ="Protection")
        additional_options = Option.objects.filter(typ="Additional")

        return render(
            request,
            "step3.html",
            {
                "car": order.car,
                "protection_options": protection_options,
                "additional_options": additional_options,
            },
        )
    elif request.method == "POST":
        for key in request.POST.keys():
            if key.startswith("option-"):
                option_id = int(key.split("-")[-1])
                option_count = int(request.POST.get(key))
                if option_count > 0:
                    option = Option.objects.get(pk=option_id)
                    op = AddedOptionInfo(option=option, count=option_count, order=order)
                    op.save()

        return redirect("cart")


@login_required
def cart(request):
    orders = request.user.orders.all()
    return render(request, "cart.html", {"orders": orders})
