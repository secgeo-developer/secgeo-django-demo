from . import views
from django.urls import path

urlpatterns = [
    path("test", views.index, name="starting-page "),  # Define the index view
]
