from operator import add
import re
from tabnanny import verbose
from django.db import models

# Create your models here.


class GeneralSetting(models.Model):
    site_name = models.CharField(
        max_length=100, default='SeçGEO', blank=True, verbose_name='Name', help_text="Enter the name of the site")
    keywords = models.CharField(
        max_length=100, default='hamdi,seçilmiş,map,harita,cbs,gps,gis,gnss,software,engineering SEO', blank=True, verbose_name='Keywords', help_text="Enter the keywords for the site")
    job_info = models.CharField(
        max_length=100, default='Job Title', blank=True, verbose_name='Job Info', help_text="Enter the job information")
    site_description = models.TextField(
        max_length=254, default='A short description about the site.', blank=True, verbose_name='Description',help_text="Enter a short description about the site")
    contact_email = models.EmailField(blank=True, verbose_name='Email',help_text="Enter the contact email address")
    phone_number = models.CharField(
        max_length=15, blank=True, verbose_name='Phone Number',help_text="Enter the phone number",)
    parameter = models.CharField(
        max_length=100, blank=True, verbose_name='Parameter',help_text="Enter any additional parameter")
    birthday = models.DateField(
        blank=True, null=True, verbose_name='Birthday', help_text="Enter the birthday")
    address = models.CharField(
        max_length=255, blank=True, verbose_name='Address', help_text="Enter the address")
    updated_date = models.DateTimeField(
        auto_now=True, blank=True, verbose_name='Updated Date')
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='Created Date')

    def __str__(self):
        # return self.site_name
        return f"{self.site_name}"


class Meta:
    verbose_name = 'General Setting'
    verbose_name_plural = 'General Settings'
    ordering = ['-created_date']
