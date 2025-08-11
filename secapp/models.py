from django.db import models

# Create your models here.
class GeneralSettings(models.Model):
    site_name = models.CharField(max_length=100,default='SeçGEO',blank=True)
    site_description = models.TextField(max_length=254,default='A short description about the site.',blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    parameter = models.CharField(max_length=100,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)  
    created_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.site_name