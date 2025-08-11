from django.shortcuts import render
from secapp.models import GeneralSetting, ImageSetting, Skill, Experience

# Create your views here.

def mainproject_context(request):
    # GeneralSetting
    site_title = GeneralSetting.objects.get(site_name='SeçGEO').parameter
    author = GeneralSetting.objects.get(site_name='base_head_author').parameter
    keywords = GeneralSetting.objects.get(
        site_name='base_head_keywords').parameter
    aboutme = GeneralSetting.objects.get(
        site_name='base_footer_about_me').parameter
    address = GeneralSetting.objects.get(
        site_name='base_banner_address').parameter
    contact_email = GeneralSetting.objects.get(
        site_name='base_banner_contact_email').parameter
    phone_number = GeneralSetting.objects.get(
        site_name='base_banner_phone_number').parameter
    birthday = GeneralSetting.objects.get(
        site_name='base_banner_birthday').parameter
    job_info = GeneralSetting.objects.get(
        site_name='base_banner_job_info').parameter
    name = GeneralSetting.objects.get(site_name='base_banner_name').parameter
    description_1 = GeneralSetting.objects.get(
        site_name='base_banner_description').parameter
    description_2 = GeneralSetting.objects.get(
        site_name='base_head_description').parameter
    myself = GeneralSetting.objects.get(
        site_name='index_myself_welcome_area').parameter
    base_welcome_area_total_projects = GeneralSetting.objects.get(
        site_name='base_welcome_area_total_projects').parameter
    base_welcome_area_total_followers = GeneralSetting.objects.get(
        site_name='base_welcome_area_total_followers').parameter
    base_welcome_area_total_volunteers = GeneralSetting.objects.get(
        site_name='base_welcome_area_total_volunteers').parameter

    # ImageSetting
    base_banner_image = ImageSetting.objects.get(
        name='base_banner_image').image_file
    base_head_favicon = ImageSetting.objects.get(
        name='base_head_favicon').image_file
    base_header_image = ImageSetting.objects.get(
        name='base_header_image').image_file

    # Skill
    skills = Skill.objects.all()

    # Experience
    experiences = Experience.objects.all()

    return {
        'site_title': site_title,
        'base_head_author': author,
        'base_head_keywords': keywords,
        'base_footer_about_me': aboutme,
        'base_banner_address': address,
        'base_banner_contact_email': contact_email,
        'base_banner_phone_number': phone_number,
        'base_banner_birthday': birthday,
        'base_banner_job_info': job_info,
        'base_banner_name': name,
        'base_banner_description': description_1,
        'base_head_description': description_2,
        'index_myself_welcome_area': myself,
        'base_banner_image': base_banner_image,
        'base_head_favicon': base_head_favicon,
        'base_header_image': base_header_image,
        'base_welcome_area_total_projects': base_welcome_area_total_projects,
        'base_welcome_area_total_followers': base_welcome_area_total_followers,
        'base_welcome_area_total_volunteers': base_welcome_area_total_volunteers,
        'skills': skills,
        'experiences': experiences
    }


def index(request):
    return render(request, 'secapp/html/index.html')


def contact(request):
    return render(request, 'secapp/html/contact.html')


def portfolio(request):
    return render(request, 'secapp/html/index.html')


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
