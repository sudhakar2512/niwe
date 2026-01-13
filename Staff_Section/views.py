from django.shortcuts import render, get_object_or_404
from django.http import request
from Staff_Section.models import StaffPhoto, CertificationStaffPhoto,\
    FinanceStaffPhoto, OwdStaffPhoto, ResearchStaffPhoto, SDTStaffPhoto,\
    TestingStaffPhoto, WRAStaffPhoto, TestingDepartStaffPhoto
from . models import CertificationAndInformationTechnologyStaff, FinanceAndAdministrationStaff, OffshoreWindDevelopStaff, ResearchAndDevelopmentStaff, SkillDevelopmentAndTrainingStaff, TestingStandardsAndRegulationStaff, WindResourceAssessmentStaff, DirectorGeneralOfficeStaff, TestingStaff

# 
def about_staff(request):
    dgStaff = DirectorGeneralOfficeStaff.objects.all().order_by('id')
    if dgStaff.exists(): 
        content = {'dgStaff': dgStaff}
        return render(request, "about_staff.html", content)


def about_staff_photo(request, dgStaff_id):
    staff = get_object_or_404(DirectorGeneralOfficeStaff, id=dgStaff_id)
    photos = StaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos':photos}
    return render (request, "staff_photo_dg.html",context)

   # 
def staff_profile_cert(request):
    staffs = CertificationAndInformationTechnologyStaff.objects.all().order_by('id')
    if staffs.exists():
        context = {'staffs': staffs}
        return render(request, "staff_profile_cert.html", context)
    return render(request, "staff_profile_cert.html")

def Certification_Staff_Photo(request, certStaff_id):
    staff = get_object_or_404(CertificationAndInformationTechnologyStaff, id=certStaff_id)
    photos = CertificationStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos':photos}
    return render (request, "staff_photo_cert.html", context)
# 
def staff_profile_fa(request):
    finStaff = FinanceAndAdministrationStaff.objects.all().order_by('id')
    if finStaff.exists():
        context = {'finStaff': finStaff}
        return render(request, "staff_profile_fa.html", context)
    return render(request, "staff_profile_fa.html")


def finance_staff_photo(request,finance_id):
    staff = get_object_or_404(FinanceAndAdministrationStaff,id=finance_id)
    photos=FinanceStaffPhoto.objects.filter(staff=staff)
    context={'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_finance.html',context)


def staff_profile_owd(request):
    owdStaff = OffshoreWindDevelopStaff.objects.all().order_by('id')
    if owdStaff.exists():
        context = {'owdStaff': owdStaff}
        return render(request, "staff_profile_owd.html", context)
    return render(request, "staff_profile_owd.html")

def owd_staff_photo(request, owd_id):
    staff = get_object_or_404(OffshoreWindDevelopStaff, id=owd_id)
    photos = OwdStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_owd.html', context)


def staff_profile_rnd(request):
    rndStaff = ResearchAndDevelopmentStaff.objects.all().order_by('id')
    if rndStaff.exists():
        context = {'rndStaff': rndStaff}
        return render(request, "staff_profile_rnd.html", context)
    return render(request, "staff_profile_rnd.html")


def rnd_staff_photo(request, rnd_id):
    staff = get_object_or_404(ResearchAndDevelopmentStaff,id= rnd_id)
    photos = ResearchStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_rnd.html', context)


def staff_profile_sdt(request):

    sdtStaff = SkillDevelopmentAndTrainingStaff.objects.all().order_by('id')
    if sdtStaff.exists():
        context = {'sdtStaff': sdtStaff}
        return render(request, "staff_profile_sdt.html", context)
    return render(request, "staff_profile_sdt.html")

def sdt_staff_photo(request, sdt_id):
    staff = get_object_or_404(SkillDevelopmentAndTrainingStaff, id=sdt_id)
    photos = SDTStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_sdt.html', context)

 
def staff_profile_snr(request):
    snrStaff = TestingStandardsAndRegulationStaff.objects.all().order_by('id')
    if snrStaff.exists():
        context = {'snrStaff': snrStaff}
        return render(request, "staff_profile_snr.html", context)
    return render(request, "staff_profile_snr.html")


def snr_staff_photo(request, snr_id):
    staff = get_object_or_404(TestingStandardsAndRegulationStaff,id= snr_id)
    photos = TestingStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_snr.html', context)


def staff_profile_wra(request):

    wraStaff = WindResourceAssessmentStaff.objects.all().order_by('id')
    if wraStaff.exists():
        context = {'wraStaff': wraStaff}
        return render(request, "staff_profile_wra.html", context)
    return render(request, "staff_profile_wra.html")


def wra_staff_photo(request, wra_id):
    staff = get_object_or_404(WindResourceAssessmentStaff,id= wra_id)
    photos = WRAStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_wra.html', context)


def staff_profile_testing(request):

    testStaff = TestingStaff.objects.all().order_by('id')
    if testStaff.exists():
        context = {'testStaff': testStaff}
        return render(request, "staff_profile_testing.html", context)
    return render(request, "staff_profile_testing.html")


def testing_staff_photo(request, testing_id):
    staff = get_object_or_404(TestingStaff,id= testing_id)
    photos = TestingDepartStaffPhoto.objects.filter(staff=staff)
    context = {'staff':staff, 'photos': photos}
    return render (request, 'staff_photo_testing.html', context)