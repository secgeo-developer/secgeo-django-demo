from django.urls import path
from contact import views

urlpatterns = [
    path('contact_form/', views.contact_form, name='contact-form'),  
    path('contact/', views.contact, name='contact-page'),  # Render the contact page  
]
