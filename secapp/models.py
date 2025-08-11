from operator import add
import re
from tabnanny import verbose
from django.db import models

# Create your models here.


class GeneralSetting(models.Model):
    site_name = models.CharField(
        max_length=100, default='SeçGEO', blank=True, verbose_name='Name', help_text="Enter the name of the site")
    site_description = models.TextField(
        max_length=254, default='A short description about the site.', blank=True, verbose_name='Description',help_text="Enter a short description about the site")
    parameter = models.TextField(
        max_length=254, blank=True, verbose_name='Parameter',help_text="Enter any additional parameter")
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
