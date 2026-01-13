from django.contrib import admin
from .models import CertificationAndInformationTechnologyStaff, ResearchAndDevelopmentStaff, WindResourceAssessmentStaff, OffshoreWindDevelopStaff, TestingStandardsAndRegulationStaff, FinanceAndAdministrationStaff, SkillDevelopmentAndTrainingStaff, DirectorGeneralOfficeStaff
from Staff_Section.models import StaffPhoto, CertificationStaffPhoto, \
    OwdStaffPhoto, TestingStaffPhoto, ResearchStaffPhoto, WRAStaffPhoto, \
    FinanceStaffPhoto, SDTStaffPhoto, TestingStaff, TestingDepartStaffPhoto
#  ####


class CnITStaffPhotoInline(admin.StackedInline):
     model = CertificationStaffPhoto
     extra = 1


class CnITStaffAdmin(admin.ModelAdmin):
     inlines = [CnITStaffPhotoInline]

     list_display = ('name', 'position', 'email', 'phone_number')
     list_filter = ('id',)
     ordering = ['id']

admin.site.register(CertificationAndInformationTechnologyStaff, CnITStaffAdmin)

# 
class StaffPhotoInline(admin.StackedInline):
     model = StaffPhoto
     extra = 1


class DGStaffAdmin(admin.ModelAdmin):
    inlines = [StaffPhotoInline]

    list_display = ('name', 'position', 'email', 'phone_number')
    ordering = ['id']
    list_filter = ('position', 'id')


admin.site.register(DirectorGeneralOfficeStaff, DGStaffAdmin)


# 
class OwdStaffPhotoInline(admin.StackedInline):
     model = OwdStaffPhoto
     extra = 1


class OWDStaffAdmin(admin.ModelAdmin):
     inlines = [OwdStaffPhotoInline]
     ordering = ['id']
     list_display = ('name', 'position', 'email', 'phone_number')


admin.site.register(OffshoreWindDevelopStaff, OWDStaffAdmin)


class TestingStaffPhotoInline(admin.StackedInline):
     model = TestingStaffPhoto
     extra = 1


class Test_StandRegulation_StaffAdmin(admin.ModelAdmin):
     inlines = [TestingStaffPhotoInline]

     list_display = ('name', 'position', 'email', 'phone_number','department')
     ordering = ['id']
     list_filter = ('id',)


admin.site.register(TestingStandardsAndRegulationStaff, Test_StandRegulation_StaffAdmin)

class RnDStaffPhotoInline(admin.StackedInline):
     model = ResearchStaffPhoto
     extra = 1

     
class RnDStaffAdmin(admin.ModelAdmin):
     inlines = [RnDStaffPhotoInline]
     
     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']
admin.site.register(ResearchAndDevelopmentStaff, RnDStaffAdmin)

# 
class  WraStaffPhotoInline(admin.StackedInline):
     model = WRAStaffPhoto
     extra = 1


class WRAStaffAdmin(admin.ModelAdmin):
     inlines = [WraStaffPhotoInline]
     list_display = ('id','name', 'position', 'email', 'phone_number')
     ordering = ['id']


admin.site.register(WindResourceAssessmentStaff, WRAStaffAdmin)


# 
class FinanceStaffPhotoInline(admin.StackedInline):
     model = FinanceStaffPhoto
     extra = 1


class FnAStaffAdmin(admin.ModelAdmin):
     inlines = [FinanceStaffPhotoInline]
     list_display = ('name', 'position', 'email', 'phone_number', 'department')
     list_filter = ('department',)
     ordering = ['id']


admin.site.register(FinanceAndAdministrationStaff, FnAStaffAdmin)

# Testing

class TestingDepartStaffPhotoInline(admin.StackedInline):
     model = TestingDepartStaffPhoto
     extra=1


class TestingStaffAdmin(admin.ModelAdmin):
     inlines = [TestingDepartStaffPhotoInline]
     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']

admin.site.register(TestingStaff, TestingStaffAdmin)


