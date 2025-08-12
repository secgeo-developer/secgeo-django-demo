from django.contrib import admin
from contact.models import Message

# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date', 'updated_date')
    search_fields = ('name', 'email', 'subject')


    class Meta:
        model = Message
        fields = '__all__'
