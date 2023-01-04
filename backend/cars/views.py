import datetime
from django.shortcuts import redirect, render
from cars.models import Car, Option, Order, AddedOptionInfo, CarDesign
from django.contrib.auth.decorators import login_required

from .utils import send_cancellation, send_invoice


def flats_details(request, pk):
    if request.method == "POST":
        car_design_id = int(request.POST.get("chosen_design"))
        car_design = CarDesign.objects.get(pk=car_design_id)
        order = Order(car_design=car_design, user=request.user)
        order.save()
        return redirect("step2", pk=order.id)
    elif request.method == "GET":
        car = Car.objects.get(pk=pk)
        car_designs = car.designs.all()
        return render(
            request,
            "sFlats.html",
            {"car": car, "car_designs": car_designs},
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
    order = Order.objects.get(pk=pk)
    if order.return_location:
        return redirect("step3", pk=pk)

    if request.method == "GET":
        return render(request, "step2.html")

    elif request.method == "POST":
        pickup_location = request.POST.get("pickup_location")
        return_location = request.POST.get("return_location")
        pickup_datetime = request.POST.get("pickup_datetime")
        return_datetime = request.POST.get("return_datetime")
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
                "car": order.car_design.car,
                "car_color": order.car_design.image_url,
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
        order.status = "ORDERED"
        order.save()
        all_orders = order.car_design.orders.filter(status="PENDING")

        other_users = []
        for order_ in all_orders:
            other_users.append(order_.user)
            order.status = "CANCELLED"
            order.save()

        other_users = list(set(other_users))
        # send_cancellation(other_users, order)
        # send_invoice(request.user, order)

        return redirect("cart")


@login_required
def cart(request):
    if request.method == "POST":
        order_id = int(request.POST.get("cancelled-order"))
        cancelled = Order.objects.get(pk=order_id)
        cancelled.status = "CANCELLED"
        cancelled.save()

    orders = request.user.orders.all()
    orders = [
        {
            "car_color": order.car_design.image_url,
            "status": order.status,
            "id": order.id,
            "car": order.car_design.car,
            "options": order.added_options_info.all(),
        }
        for order in orders
    ]
    return render(request, "cart.html", {"orders": orders})
