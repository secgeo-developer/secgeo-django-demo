from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from secapp.models import Education, GeneralSetting, ImageSetting, Skill, Experience, SocialMedia, Document

# Create your views here.


def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(site_name=parameter).parameter
    except:
        obj = ''
    return obj


def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).image_file
    except:
        obj = ''
    return obj


def mainproject_context(request):
    # GeneralSetting
    site_title = get_general_setting('site_title')
    author = get_general_setting('base_head_author')
    keywords = get_general_setting('base_head_keywords')
    aboutme = get_general_setting('base_footer_about_me')
    address = get_general_setting('base_banner_address')
    contact_email = get_general_setting('base_banner_contact_email')
    phone_number = get_general_setting('base_banner_phone_number')
    birthday = get_general_setting('base_banner_birthday')
    job_info = get_general_setting('base_banner_job_info')
    name = get_general_setting('base_banner_name')
    description_1 = get_general_setting('base_banner_description')
    description_2 = get_general_setting('base_head_description')
    myself = get_general_setting('index_myself_welcome_area')
    base_welcome_area_total_projects = get_general_setting(
        'base_welcome_area_total_projects')
    base_welcome_area_total_followers = get_general_setting(
        'base_welcome_area_total_followers')
    base_welcome_area_total_volunteers = get_general_setting(
        'base_welcome_area_total_volunteers')

    # ImageSetting
    base_banner_image = get_image_setting('base_banner_image')
    base_head_favicon = get_image_setting('base_head_favicon')
    base_header_image = get_image_setting('base_header_image')

    # Skill
    skills = Skill.objects.all()

    # Experience
    experiences = Experience.objects.all()

    # Education
    educations = Education.objects.all()

    # Social Media
    social_media = SocialMedia.objects.all()

    # Document
    documents = Document.objects.all()

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
        'experiences': experiences,
        'educations': educations,
        'social_media': social_media,
        'documents': documents
    }


def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def aboutus(request):
    return render(request, 'about-us.html')


def elements(request):
    return render(request, 'elements.html')


def blog(request):
    return render(request, 'blog.html')


def singleBlog(request):
    return render(request, 'single-blog.html')


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)
   # doc = Document.objects.get(slug=slug)
   # if doc:
   #     return redirect(doc.file.url)
   # else:
   #     return redirect('index')
