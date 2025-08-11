from tkinter import E
from turtle import up
from django.contrib import admin

from .models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia

# Register your models here.


@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_description',
                    'parameter', 'created_date', 'updated_date')
    search_fields = ('site_name', 'parameter')
    # list_editable = ('site_description', 'contact_email', 'phone_number','parameter')

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
    list_display = ('id', 'name', 'percentage', 'order',
                    'updated_date', 'created_date')
    search_fields = ('name', 'order', 'percentage')

    class Meta:
        model = Skill
        fields = '__all__'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_title',
                    'position', 'start_date', 'end_date')
    search_fields = ('company_name', 'job_title', 'position')

    class Meta:
        model = Experience
        fields = '__all__'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'department',
                    'position', 'start_date', 'end_date')
    search_fields = ('school_name', 'department', 'position')

    class Meta:
        model = Education
        fields = '__all__'


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'icon')
    search_fields = ('link', 'icon')

    class Meta:
        model = SocialMedia
        fields = '__all__'