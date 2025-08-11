from django.contrib import admin

from .models import GeneralSetting

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_description', 'contact_email', 'phone_number', 'parameter', 'created_date', 'updated_date')
    search_fields = ('site_name', 'contact_email', 'phone_number','parameter')
    #list_editable = ('site_description', 'contact_email', 'phone_number','parameter')
    class Meta:
        model = GeneralSetting
        fields = '__all__'
