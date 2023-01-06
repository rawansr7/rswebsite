from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from user.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def signup(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    # get information from request
    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["pass"]

    # check if user is already in the database
    users = User.objects.all()
    users_emails = [user.email for user in users]
    if email in users_emails:
        return JsonResponse(
            {"error": "A user with the same email address already exists"}
        )

    # create user
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

    # get information from request
    email = request.POST["email"]
    password = request.POST["pass"]

    # check if user is in the database
    users = User.objects.all()
    users_emails = [user.email for user in users]
    if email not in users_emails:
        return JsonResponse({"error": "This user does not exist in our database"})

    # check password
    user = authenticate(request, username=email, password=password)
    if user is None:
        return JsonResponse({"error": "Incorrect password."})

    # login the user: creates a session in the database
    auth_login(request, user)

    return JsonResponse({})


def logout(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    # logouts the user: deletes the session in the database
    auth_logout(request)
    return JsonResponse({})
