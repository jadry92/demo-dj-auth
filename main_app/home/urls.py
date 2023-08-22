""" Home URLs """

# Django
from django.urls import path

# Views
from main_app.home.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]