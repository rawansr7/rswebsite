from django.shortcuts import render
from cars.models import Car
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from user.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


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


def signup(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["pass"]

    users = User.objects.all()
    users_emails = [user.email for user in users]
    if email in users_emails:
        return JsonResponse(
            {"error": "A user with the same email address already exists"}
        )

    User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=fname,
        last_name=lname,
    )
    return JsonResponse({})


def login(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    email = request.POST["email"]
    password = request.POST["pass"]

    users = User.objects.all()
    users_emails = [user.email for user in users]
    if email not in users_emails:
        return JsonResponse({"error": "This user does not exist in our database"})
    user = authenticate(request, username=email, password=password)
    if user is None:
        return JsonResponse({"error": "Incorrect password."})

    auth_login(request, user)
    return JsonResponse({})


def logout(request):
    if request.method != "POST":
        return HttpResponseBadRequest
    auth_logout(request)
    return JsonResponse({})
