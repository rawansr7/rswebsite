from .views import (
    flats_details,
    all_flats,
    reservation,
    step1,
    step2,
    step3,
    cart,
    home,
    about,
    contact,
)
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path(
        "contact",
        contact,
        name="contactus",
    ),
    path("flats", all_flats, name="flats"),
    path("flats/<int:pk>", flats_details, name="sflats"),
    path("reservation", reservation, name="reservation"),
    path("reservation/step1", step1, name="step1"),
    path("reservation/step2/<int:pk>", step2, name="step2"),
    path("reservation/step3/<int:pk>", step3, name="step3"),
    path("cart", cart, name="cart"),
]
