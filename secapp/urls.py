from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="starting-page"),  # Define the index view
]
