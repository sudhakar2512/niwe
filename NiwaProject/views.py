from django.http import HttpResponse, request
from django.db.models import F, IntegerField, ExpressionWrapper
from django.db.models.functions import Cast
from django.shortcuts import render, redirect, get_object_or_404
from about_section.models import *
from Document_Section.models import *
from django.db import models

from Depart_Section.models import *
from home_sections.models import *
from django.contrib.auth import authenticate, login
from django_otp.forms import OTPAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm



def index(request):
    dgm = DirectorGeneralMessage.objects.all()
    mnre_entry = MNRE_WhatsNew.objects.all().order_by('-id')[:5]
    Events_entry = Events_New.objects.all()
    whatsnew_entry = WhatsNew.objects.all().order_by('-id')[:5]
    running_news_entry = Running_News.objects.all().order_by('-id')
   
    context = {'dgm': dgm, 'mnre_entry':mnre_entry, 'Events_entry':Events_entry,'whatsnew_entry': whatsnew_entry,'running_news_entry' : running_news_entry}
    return render(request, "index.html",context)


# sitemap
def sitemap(request):
    return render(request, 'sitemap.html')


def department_srra_online_training(request):
      return render(request, "department_srra_online_training.html")


def fowpi_report(request):
    return render(request, "fowpi_report.html")


def fowpi_workshop_presentation(request):
    return render(request, "fowpi_workshop_presentation.html")


def gallery(request):
    return render(request, "gallery.html")





def international_conference_wsra(request):
    return render(request, "international_conference_wsra.html")


def international_workshop_ppt(request):
    return render(request, "international_workshop_ppt.html")




def offshore_EPD_Gujarat(request):
    return render(request, "offshore_EPD_Gujarat.html")


def pan_india_workshop(request):
    return render(request, "pan-india_workshop.html")


def services(request):
    return render(request, "services.html")


def small_wind_energy_hybrid_system_presentation(request):
    return render(request, "small_wind_energy_&_hybrid_system_presentation.html")


def sub_gallery(request):
    return render(request, "sub-gallery.html")


def tenders(request):
    return render(request, "tenders.html")


def wind_potential(request):
    return render(request, "wind_potential.html")


def glossery(request):
    return render(request, "glossary.html")


def disclaimer(request):
    return render (request, "disclaimer.html")






# screen-reader-access
def Screen_Reader(request):
    return render(request, "screen-reader-access.html")

 
#  all side-tabs
def Academy(request):
    return render(request, 'tab-academic.html')


# library
def Library(request):
    Library = SDT_Library.objects.all()
    lib = Library_Sub_Data.objects.all().order_by('id') 
    context = {
        "Library":Library, "lib":lib
    }
    return render (request, 'tab-library.html', context)

# 
def ITEC_training(request):
    return render (request, 'tab-ITEC.html')


def ITEC_trainings(request):
    trainings = SDT_Eitc_Trainings.objects.all().order_by('id')
    context = {
        "trainings": trainings
    }
    return render (request, 'tab-ITEC-training.html', context)


def ITEC_trainings_sub(request, training_id):
    item = get_object_or_404(SDT_Eitc_Trainings, id=training_id)
    sub_training = SDT_Eitc_Sub_Training.objects.filter(item=item).order_by('id')
    context = {
        "sub_training": sub_training, "item":item
    }
    return render (request, 'tab-ITEC-training-sub.html', context)


def ITEC_training_countries(request):
    return render (request, 'tab-ITEC-countries.html')


def ITEC_training_feedback(request):
    return render (request, 'tab-ITEC-feedback.html')


def short_term_course(request):
    short = SDT_Short_Term.objects.all()
    context = {"short": short}
    return render (request, 'tab-short.html', context)


def training_calander(request):
    national = SDT_Training_calender.objects.all()
    return render (request, 'tab-calender.html', {"national": national})


def training_calander_sub(request, data_id):
    item = get_object_or_404(SDT_Training_calender, id=data_id)
    national_data = SDT_Training_Sub_calender.objects.filter(item=item).order_by('id')
    content = {"item": item, "national_data":national_data}
    return render(request, "tab-calender-sub.html", content)


def global_wind_day(request):
    globals = SDT_GlobalWindDay.objects.all().order_by('id')
    context = {"globals": globals}
    return render (request, 'tab-global.html', context)

def gloabl_sub_wind_day(request, global_id):
    item=get_object_or_404(SDT_GlobalWindDay, id=global_id)
    sub_global = SDT_Global_Sub_Wind.objects.filter(item=item).order_by('id')
    context={
        "sub_global":sub_global, "item":item
    }
    return render (request, 'tab-global-sub.html', context)


def ireda_niwe_annual_awards(request):
    ireda= SDT_Iredas_News.objects.all().order_by('-id')
    context= {
        "ireda" : ireda
    }
    return render(request, "ireda_niwe_annual_awards.html", context)

def ireda_niwe_annual_subawards(request, year):
    item = get_object_or_404(SDT_Iredas_News, year=year )
    subIreda = SDT_Iredas_Sub_News.objects.filter(item=item).order_by('id')
    context = {
        "subIreda" : subIreda, "item" : item
    }
    
    return render (request, 'ireda_niwe_annual_awards_sub.html', context)

def webinar(request):
    webinar = SDT_Webinar.objects.all()
    context = {"webinar": webinar}
    return render (request, 'tab-webinar.html', context)


# 
def offshore_lidar(request):
    return render (request, 'tab_offshore_lidar.html')


# 
def fowind_report(request):
    return render (request, 'tab-fowind_report.html')
# 

 
def workshop_confrence(request):
    workshop = SDT_workshop.objects.all()
    
    content = {"workshop": workshop}
    return render (request, 'tab-workshop.html', content)


def workshop_confrence_images(request, workshop_id):
   
    item = get_object_or_404(SDT_workshop, id=workshop_id)
    photos = SDT_workshop_type.objects.filter(item=item).order_by('id')
    content = {"item": item, "photos":photos}
    return render(request, "tab-workshop_photo.html", content)


def customize_training(request):
    customize = SDT_Customize_Training.objects.all().order_by('-serial')
    return render (request, 'tab-customized.html', {"customize":customize})


def customize_training_sub(request, id):
    item = get_object_or_404(SDT_Customize_Training, id=id)
    custom = SDT_Customize_Training_Sub.objects.filter(item=item).order_by('id')
    content = {"item": item, "custom":custom}
    return render(request, "tab-customized_sub.html", content)


def national_training(request):
    national = SDT_National.objects.all().order_by('-id')
    return render(request, 'tab-national.html', {"national": national})


def national_training_data(request, slug):
    item = get_object_or_404(SDT_National, slug=slug)
    national_data = SDT_National_Page.objects.filter(item=item).order_by('id')
    content = {"item": item, "national_data": national_data}
    return render(request, "tab-national-data.html", content)


def training_list(request):
    trainings = SDT_InternationalTraining.objects.all()
    return render(request, 'tab-international.html', {'trainings': trainings})


def eitec_detail(request, training_slug):
    training = get_object_or_404(SDT_InternationalTraining, slug=training_slug)
    eitecs = SDT_InternationalTraining_eitec.objects.filter(item=training)
    return render(request, 'tab-international-eitc.html', {'training': training, 'eitecs': eitecs})


def sub_eitec_detail(request, eitec_slug):
    eitec = get_object_or_404(SDT_InternationalTraining_eitec, slug=eitec_slug)
    sub_eitecs = SDT_InternationalTraining_sub_eitec.objects.filter(eitec=eitec)
    return render(request, 'tab-international-sub-eitc.html', {'eitec': eitec, 'sub_eitecs': sub_eitecs})


# 
def vayumitra_sdt(request):
    vayumitra = SDT_vayumitra.objects.all().order_by('id')
    content = {"vayumitra": vayumitra}
    return render (request, 'tab-vayumitra_sdt.html', content)


def newsletters(request):
    news = Newsletters.objects.all().order_by('-issue')
    context = {'news': news}
    return render (request, 'tab-news.html', context)


def news_letter_reports_details(request, issue):
    report = get_object_or_404(Newsletters, issue=issue)
    return render(request, 'tab_newsletter_reports_details.html', {'report': report, 'issue': issue, 'year': report.year})

# annual_reports :
def annual_reports(request):
    annual = AnnualReport.objects.all().order_by('-year')
    context = {'annual': annual}
    return render (request, 'tab-annual.html', context)

def annual_reports_details(request, year):
    report = get_object_or_404(AnnualReport, year=year)
    return render(request, 'tab_annual_reports_details.html', {'report': report, 'year': year})



def events_update(request):
    return render (request, "Niwe_events.html")

def whatsNew(request):
    return render (request, "whats_new.html")

def corporate_film_hindi(request):
    return render(request, 'corporate_film.html')

# def technical_reports(request):
#     tech_reports = techreports.objects.all().order_by('id')    
#     context = {'tech_reports': tech_reports}
#     return render(request, "technical_reports.html", context)

def technical_reports(request):
    categories = TechnicalReportCategory.objects.prefetch_related('files').all()
    return render(request, 'technical_reports.html', {'categories': categories})

def rfd(request):
    return render (request, 'rfd.html')

def search_results(request):    
    return render (request, 'search_results.html')



def help_page(request):    
    return render (request, 'help_page.html')