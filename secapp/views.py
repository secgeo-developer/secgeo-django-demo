from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'secapp/html/index.html')


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
