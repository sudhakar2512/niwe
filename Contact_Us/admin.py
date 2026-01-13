from django.contrib import admin
from . models import ContactUs

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('feedback_and_Address', 'testing_and_Research_Station')
    ordering = ['id']
