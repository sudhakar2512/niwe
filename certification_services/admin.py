from django.contrib import admin
from . models import Certification_Procedure

# Register your models here.


@admin.register(Certification_Procedure)
class GenInfoAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    list_filter = ('id',)

    ordering = ['id']
