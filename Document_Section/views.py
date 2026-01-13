from django.http import request
from . models import *

from django.shortcuts import render, get_object_or_404


# documents
def download(request):
    documents = Documents.objects.all().order_by('id')
    if documents.exists():
       context = {'documents': documents}
       return render(request, "downloads.html", context)
    return render(request, "downloads.html")


# record retention
def record_retention(request):
    record = RecordsRetentionSchedule.objects.all().order_by('id')
    if record.exists():
        context = {'record': record}
        return render(request, "record_retention.html", context)
    return render(request, "record_retention.html")

def information_weg_installation(request):
    return render(request, "information_weg_installation.html")

def weg_install_country_wise(request):
    country_wise = weg_install_world_wise.objects.all()
    return render(request, "info_weg_install_details_country_wise.html", {'country_wise':country_wise})


def weg_install_India(request):
    details = WEG_Installation_Details_India.objects.all()
    return render(request, "info_weg_install_details_India.html", {'details': details})


# related links
# def relatedlinks(request):

#     relLinks = RelatedLinks.objects.all().order_by('id')
#     if relLinks.exists():
#         context = {'relLinks': relLinks}
#         return render(request, 'relatedlinks.html', context)
#     return render(request, "relatedlinks.html")

# general info
# def information_gi(request):
#     info = GeneralInformation.objects.all().order_by('id')
#     compare = ComparisonBetweenFosilFuelAndWind.objects.all().order_by('id')

    # if info.exists() and compare.exists():
#         context = {'info': info, 'compare': compare}
#         return render(request, "information_gi.html", context) 
#     return render(request, "information_gi.html")


# 
def information_gi(request):
    info = GeneralInformation.objects.all().order_by('id')
    if info.exists():
        context = {'info': info}
        return render(request, "information_gi.html", context) 
    return render(request, "information_gi.html")


# revised info
def information_hwed(request):
    revise = RevisedGuidelineForProject.objects.all().order_by('id')
    # if revised.exists():
    context = {'revise': revise}
    return render(request, "information_hwed.html", context)


# faqs
def faq(request):
    faqs = FAQs.objects.all().order_by('id')

    if faqs.exists():
        context = {'faqs': faqs}
        return render(request, "faq.html", context)
    return render(request, "faq.html")


# azadi
def azadi_ka_amrit_mahotsav(request):
    report = AnnualReport.objects.all().order_by('id')
    context = {'report': report}
    return render(request, "azadi_ka_amrit_mahotsav.html", context)


#  power policy :
def wind_power_policy(request):
    return render (request, 'wind_power_policy.html')


def event_schedule_22_23(request):
    akamevents = AKAM_Events_22_23.objects.all().order_by('id')  # Fetch all events
    return render(request, 'amrit-mahotsav-22-23.html', {'akamevents': akamevents})

def report_detail_22_23(request,event_id):
    event_report = get_object_or_404(AKAM_Events_22_23,id=event_id)
    return render(request,'report_detail_22_23.html',{'event_report':event_report})

def event_schedule_21_22(request):
    akamevents = AKAM_Events_21_22.objects.all().order_by('start_date')
    return render(request,'amrit-mahotsav-21-22.html', {'akamevents': akamevents})

def report_detail_21_22(request,event_id):
    event_report = get_object_or_404(AKAM_Events_21_22,id=event_id)
    return render(request,'report_detail_21_22.html',{'event_report':event_report})

