from django.contrib import admin
from .models import *

@admin.register(RightToInformation)
class RtiAdmin(admin.ModelAdmin):

    list_display = ( 'year', 'document')
    list_filter = ('id',)
    ordering = ['id']

class InformationInline(admin.StackedInline):
    model =subInformation
    extra =1 

class InfoAdmin(admin.ModelAdmin):
    inlines= [InformationInline]
    list_display=('title','id',)
    list_filter  =  ('id',)
    search_fields  =  ('title', 'id',)
    ordering  =  ['serial']
    
admin.site.register(Information, InfoAdmin)

class AuditReportAdmin(admin.ModelAdmin):
    list_display = ('id','year','pdf_link')
    list_filter = ('year',)
    ordering = ('year',)
admin.site.register(AuditReport,AuditReportAdmin)

class AnnualAccountAdmin(admin.ModelAdmin):
    list_display = ('id','year','pdf_link')
    list_filter = ('year',)
    ordering = ('year',)
admin.site.register(AnnualAccount,AnnualAccountAdmin)

class GCminutesAdmin(admin.ModelAdmin):
    list_display = ('id','title','pdf_link')
    list_filter = ('title',)
    ordering = ('title',)
admin.site.register(GCminutes,GCminutesAdmin)

class FinanceReportAdmin(admin.ModelAdmin):
    list_display = ('id','year','pdf_link')
    list_filter = ('year',)
    ordering = ('year',)
admin.site.register(FinanceReport,FinanceReportAdmin)

class RTIApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','application_year','pdf_link')
    list_filter = ('application_year',)
    ordering = ('application_year',)
admin.site.register(RTIApplication,RTIApplicationAdmin)


class RTI_HODAdmin(admin.ModelAdmin):
    list_display = ('s_no','Name','Designation','From_Date','To_Date','Remarks')
    list_filter = ('Name',)
    ordering = ('s_no',)
admin.site.register(RTI_HOD,RTI_HODAdmin)

class RTI_TourDetailInline(admin.StackedInline):
    model = RTI_Tour_details
    extra = 1

class RTI_Tour_typeAdmin(admin.ModelAdmin):
    inlines = [RTI_TourDetailInline]    
    ordering = ('id',)
admin.site.register(RTI_Tour_type,RTI_Tour_typeAdmin)

class CitizenAdmin(admin.ModelAdmin):
    list_display = ('id',)    
    ordering = ('id',)
    
admin.site.register(Citizen,CitizenAdmin)

class Public_info_OfficersAdmin(admin.ModelAdmin):
    list_display = ('id',)    
    ordering = ('id',)

admin.site.register(Public_info_Officers,Public_info_OfficersAdmin)
