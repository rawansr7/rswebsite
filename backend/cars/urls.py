from django.views.generic import TemplateView
from .views import flats_details, all_flats
from django.urls import path

urlpatterns = [
    path("", TemplateView.as_view(template_name="homePage.html"), name="home"),
    path("about", TemplateView.as_view(template_name="aboutUs.html"), name="about"),
    path("flats", all_flats, name="flats"),
    path("flats/<int:pk>", flats_details, name="sflats"),
]
