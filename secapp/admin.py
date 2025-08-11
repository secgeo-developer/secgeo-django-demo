from turtle import up
from django.contrib import admin

from .models import GeneralSetting, ImageSetting, Skill

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_description','parameter', 'created_date', 'updated_date')
    search_fields = ('site_name', 'parameter')
    #list_editable = ('site_description', 'contact_email', 'phone_number','parameter')
    class Meta:
        model = GeneralSetting
        fields = '__all__'



@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_file')
    search_fields = ('name', 'description')
    class Meta:
        model = ImageSetting
        fields = '__all__'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'percentage', 'order', 'updated_date','created_date')
    search_fields = ('name','order','percentage')
    class Meta:
        model = Skill
        fields = '__all__'