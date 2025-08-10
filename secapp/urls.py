from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="starting-page"),
    path('contact', views.contact, name="contact-page"),  # Define the index view
    path('portfolio', views.portfolio, name="portfolio-page"),
    path('services', views.services, name='services-page'),
    path('about-us', views.aboutus, name='aboutus-page'),
    path('elements', views.elements, name='elements-page')
]
