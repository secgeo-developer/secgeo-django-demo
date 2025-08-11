from django.shortcuts import render
from secapp.models import GeneralSetting

# Create your views here.


def index(request):
    site_title = GeneralSetting.objects.get(site_name='SeçGEO').site_name
    parameter = GeneralSetting.objects.get(site_name='SeçGEO').parameter
    site_test = GeneralSetting.objects.get(site_name='site_test').parameter
    job_info = GeneralSetting.objects.get(site_name='SeçGEO').job_info
    birthday = GeneralSetting.objects.get(site_name='SeçGEO').birthday
    address = GeneralSetting.objects.get(site_name='SeçGEO').address
    keywords = GeneralSetting.objects.get(site_name='SeçGEO').keywords
    phone_number = GeneralSetting.objects.get(site_name='SeçGEO').phone_number
    contact_email = GeneralSetting.objects.get(site_name='SeçGEO').contact_email
    context = {
        'site_title': site_title,
        'parameter': parameter,
        'site_test': site_test,
        'job_info': job_info,
        'birthday': birthday,
        'address': address,
        'phone_number': phone_number,
        'contact_email': contact_email,
        'keywords': keywords
    }
    return render(request, 'secapp/html/index.html', context=context)


def contact(request):
    return render(request, 'secapp/html/contact.html')


def portfolio(request):
    return render(request, 'secapp/html/portfolio.html')


def services(request):
    return render(request, 'secapp/html/services.html')


def aboutus(request):
    return render(request, 'secapp/html/about-us.html')


def elements(request):
    return render(request, 'secapp/html/elements.html')


def blog(request):
    return render(request, 'secapp/html/blog.html')


def singleBlog(request):
    return render(request, 'secapp/html/single-blog.html')
