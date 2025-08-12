import re
from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
from contact.forms import ContactForm

# Create your views here.


def contact_form(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            contact_form.send_email()

            success = True
            message_ = 'Contact Form sent successfully!'
        else:
            success = False
            message_ = 'Contact Form is not valid.'
    else:
        success = False
        message_ = 'Request method is not valid.'

    context = {
        'success': success,
        'message': message_,
    }
    return JsonResponse(context)


def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'secapp/html/contact.html', context)
