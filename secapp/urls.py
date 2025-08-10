from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="starting-page"),  
    path('contact', views.contact, name="contact-page") # Define the index view
]
