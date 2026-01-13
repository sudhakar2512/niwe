from django.contrib import admin
from .models import Departments, Reserach_n_Development, Testing_and_Standards_Regulation, Wind_Resources_Assessment, Offshore_Wind_Development, Finance_and_Administration, Skill_developements_training
from  . models import *
# 
# class ImageInline(admin.StackedInline):
#     model = Image

    
@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('id',)

    list_display = ('title', 'description')
    ordering = ['id']


# sdt
@admin.register(Skill_developements_training)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('id',)
    
    ordering = ['id']


# 
@admin.register(Reserach_n_Development)
class RnDAdmin(admin.ModelAdmin):
    search_fields = ('id',)

    list_display = ('title', 'description')
    ordering = ['id']


@admin.register(Testing_and_Standards_Regulation)
class TestingAdmin(admin.ModelAdmin):
    # list_display = ('title', 'description', 'document_File')
    list_display = ('title', 'description')
    search_fields = ('id',)
    list_filter = ('id',)
    
    ordering = ['id']

@admin.register(Testing_menu)
class TestingMenuAdmin(admin.ModelAdmin):
    # list_display = ('title', 'description', 'document_File')
    list_display = ('title', 'description')
    search_fields = ('id',)
    list_filter = ('id',)
    
    ordering = ['id']

@admin.register(depart_documents)
class departdocumentsAdmin(admin.ModelAdmin):
    list_display = ('Description','Version','Download')
    search_fields = ('id',)
    list_filter = ('id',)    
    ordering = ['id']


class WindTerBinephotoAdmin(admin.ModelAdmin):
    list_display = ('image')
    search_fields = ('id',)
    list_filter = ('id',)
    ordering = ['id']
admin.site.register(Wind_Terbine_photo)
# 
class Department_Testing_TypeInline(admin.StackedInline):
    model = Department_testing_measureType
    extra = 1

@admin.register(Department_testing_measure)
class DepartTestingMeasureAdmin(admin.ModelAdmin):
    inlines = [Department_Testing_TypeInline]
    search_fields = ('id',)
    list_filter = ('id',)
    
    ordering = ['id']   


# 
class Workshop_SDT_PhotosInline(admin.StackedInline):
    model = SDT_workshop_type
    extra = 1


@admin.register(SDT_workshop)
class Workshop_SDT(admin.ModelAdmin):
    inlines = [Workshop_SDT_PhotosInline]
    search_fields = ('id',)
    list_filter = ('id',)
    
    ordering = ['id']   
# 


class SDT_Customized_TrainingInline(admin.StackedInline):
    model = SDT_Customize_Training_Sub
    extra = 1

    
@admin.register(SDT_Customize_Training)
class Customized_Training(admin.ModelAdmin):
    inlines = [SDT_Customized_TrainingInline]
    search_fields=('id', )
    list_display = ('title','serial',)
    ordering = ['serial']


class SDT_Nationals_pagesInline(admin.StackedInline):
    model = SDT_National_Page
    extra = 0

@admin.register(SDT_National)
class SDT_NationalsAdmin(admin.ModelAdmin):
    inlines = [SDT_Nationals_pagesInline]
    list_display = ('serial', 'slug','title','New_Label')  # Include 'slug' in the list display
    # search_fields = ('title', 'slug')  # Allow searching by title or slug
    # list_filter = ('slug',)  # Add filter option by slug
    ordering = ['-id']  # Default ordering by serial

# 
class SDT_TrainingInline(admin.StackedInline):
    model = SDT_Training_Sub_calender
    extra = 1


@admin.register(SDT_Training_calender)
class SDT_TrainingCalender(admin.ModelAdmin):
    inlines = [SDT_TrainingInline]
    list_display = ('id', 'description',)
    search_fields = ('id', 'serial',)
    list_filter = ('id',)
    ordering = ['id']


class SDT_EITC_TrainingInline(admin.StackedInline):
    model = SDT_Eitc_Sub_Training
    extra = 1


@admin.register(SDT_Eitc_Trainings)
class SDT_EITC_Training(admin.ModelAdmin):
    inlines = [SDT_EITC_TrainingInline]
    list_display = ('id', 'project_title',)
    search_fields = ('id', 'serial',)
    list_filter = ('id',)
    ordering = ['id']


@admin.register(SDT_Library)
class SDT_Libraries(admin.ModelAdmin):
    list_display = ('title_type', 'serial', 'id',)
    search_fields = ('title_type', 'serial', 'id',)
    list_filter = ('id', 'title_type',)
    ordering = ['id']


class SDT_InternationalTrainingSubEitecInline(admin.StackedInline):  # You can also use TabularInline for a table format
    model = SDT_InternationalTraining_sub_eitec
    extra = 1  # Number of extra forms shown by default


class SDT_InternationalTrainingEitecInline(admin.StackedInline):
    model = SDT_InternationalTraining_eitec
    extra = 1  # Number of extra forms shown by default
    inlines = [SDT_InternationalTrainingSubEitecInline]


@admin.register(SDT_InternationalTraining)
class SDTInternationalTrainingAdmin(admin.ModelAdmin):
    inlines = [SDT_InternationalTrainingEitecInline]
    list_display = ('title',)
    ordering = ['id']
    search_fields = ('id',)


# Register other models individually if needed
# admin.site.register(SDT_InternationalTraining_eitec)
admin.site.register(SDT_InternationalTraining_sub_eitec)


# 
@admin.register(Wind_Resources_Assessment)
class Wind_Res_Admin(admin.ModelAdmin):
    search_fields = ('id',)

    list_display = ('title', 'description')
    ordering = ['id']
    # inlines = [ImageInline]


# class RelatedImageInline(admin.StackedInline):
#     model = RelatedImage

    
@admin.register(WRA_Sale_publication)
class Wra_Sale_publications(admin.ModelAdmin):
    list_display = ('product', 'serial', 'price',)
    search_fields = ('id', 'serial',)
    ordering = ['serial']

    
@admin.register(Department_Fna_Finance)
class Department_FNA_Finances(admin.ModelAdmin):
    list_display = ('title', 'id',)
    search_fields = ('id', 'title',)
    ordering = ['id']


@admin.register(Department_Fna_Purchase)
class Department_FNA_Purchases(admin.ModelAdmin):
    list_display = ('annexure', 'id',)
    search_fields = ('id', 'annexure',)
    ordering = ['id']
    
    
@admin.register(WRA_srra_stations)
class Wra_Srra_Stations(admin.ModelAdmin):
    list_display = ('serial', 'state_ut',)
    search_fields = ('id',)
    ordering = ['id']


@admin.register(WRA_Numeric_Wind)
class WRA_Numeric(admin.ModelAdmin):
    list_display = ('domain', 'number_station',)
    search_fields = ('serial',)
    ordering = ('id',)

    
@admin.register(WRA_Micro_Servey)
class WRA_Servey(admin.ModelAdmin):
    list_display = ('state',)
    search_fields = ('serial',)
    ordering = ('id',)

    
@admin.register(WRA_Estimated_Potential)
class WRA_Power_Potential(admin.ModelAdmin):
    list_display = ('serial',)
    search_fields = ('serial',)
    list_filter = ('id',)
    
    ordering = ('id',)
    
    
@admin.register(WRA_Srra_Station_phases)
class Wra_Srra_phase(admin.ModelAdmin):
    
    search_fields = ('station_id', 'id',)
    list_display = ('station_id',)
    list_filter = ('id',)
    ordering = ['id']

    
@admin.register(WRA_Srra_Station_phaseII)
class Wra_Srra_phaseII(admin.ModelAdmin):
    
    search_fields = ('station_id', 'id',)
    list_display = ('station_id',)
    list_filter = ('id',)
    ordering = ['id']

    
@admin.register(WRA_Srra_Station_meda)
class Wra_Srra_phase_meda(admin.ModelAdmin):
    
    search_fields = ('station_id', 'id',)
    list_display = ('station_id',)
    list_filter = ('id',)
    ordering = ['id']

    
@admin.register(WRA_Srra_Station_anert)
class Wra_Srra_phase_anert(admin.ModelAdmin):
    
    search_fields = ('station_id', 'id',)
    list_display = ('station_id',)
    list_filter = ('id',)
    ordering = ['id']

    
@admin.register(WRA_Srra_Station_ams)
class Wra_Srra_phase_ams(admin.ModelAdmin):
    
    search_fields = ('station_id', 'id',)
    list_display = ('station_id',)
    list_filter = ('id',)
    ordering = ['id']

    
# 
@admin.register(Offshore_Wind_Development)
class OwdAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']
    list_filter = ('id', 'title',)
    search_fields = ('title', 'id',)
    # inlines = [RelatedImageInline]


@admin.register(Finance_and_Administration)
class FnAdmin(admin.ModelAdmin):
    list_display = ('description', 'NIWE_Pan_ARN_GST_Details')
    list_filter = ('id',)


# class VayumitraSubInline(admin.StackedInline):
#     model = SDT_Vayumitra_sub
#     extra = 1


@admin.register(SDT_vayumitra)
class VayumitraAdmin(admin.ModelAdmin):
    # inlines = [VayumitraSubInline]
    list_filter = ('id',)
    list_display = ( 'title','id',)
    search_fields = ('id',)
    
    ordering = ['id']


class SDT_Global_SubInline(admin.StackedInline):
    model = SDT_Global_Sub_Wind
    extra = 1


@admin.register(SDT_GlobalWindDay)
class SDT_Global(admin.ModelAdmin):
    inlines = [SDT_Global_SubInline]
    list_display = ('title','serial','id',)
    ordering = ['id']


class SDT_Ireda_SubInline(admin.StackedInline):
    model = SDT_Iredas_Sub_News
    extra = 1


@admin.register(SDT_Iredas_News)
class SDT_Ireda(admin.ModelAdmin):
    inlines = [SDT_Ireda_SubInline]
    list_display = ('serial','year','title')
    search_fields = ('serial','year')
    ordering = ['id']




@admin.register(SDT_Webinar)
class SDT_Webinars(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']


@admin.register(SDT_Short_Term)
class ShortTermCourses(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']

@admin.register(WindPotentialSite)
class WindPotentialSiteAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'jpg_map', 'kml_file')  # Display these fields
    search_fields = ('state_name',)  # Search by state name