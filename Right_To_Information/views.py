from django.shortcuts import render, get_object_or_404
from .models import *

def rti(request):

    rti = RightToInformation.objects.all().order_by('-year')
    info= Information.objects.all().order_by('id')
    finance_info = FinanceReport.objects.all().order_by('-year')
    
    context = {
        'rti': rti, "info"  :info, "finance_info" : finance_info
                }
    return render(request, "rti.html", context)


def subInfo(request, info_id):
    item = get_object_or_404(Information, id=info_id)
    subInfo = subInformation.objects.filter(item=item).order_by('id')
  
    context = {
        "subInfo" : subInfo, "item": item
    }
    return render(request, "rti-sub.html", context)

# RTI page audit report
def audit_report(request):
    report = AuditReport.objects.all().order_by('-year')
    return render(request, "audit_report.html",{'report':report})

def audit_report_description(request,year):
    detail = get_object_or_404(AuditReport, year=year)
    return render(request, "audit_report_detail.html",{'detail':detail})
    
# RTI page annual account
def annual_account(request):
    account = AnnualAccount.objects.all().order_by('-year')
    return render(request, "annual_accounts.html",{'account':account})

# RTI page Governing council menu
def rti_governing_council(request):    
    return render(request, "rti_governing_council.html")

# RTI page Governing council--Minutes of GC menu
def minutes_GC(request):
    report = GCminutes.objects.all().order_by('-id')
    return render(request, "minutes_GC.html",{'report':report})

# RTI page Governing council--Minutes of GC menu
def rti_application(request):
    report = RTIApplication.objects.all().order_by('-application_year')
    return render(request, "rti_application.html",{'report':report})

# RTI page HOD
def rti_HOD(request):
    HOD_details = RTI_HOD.objects.all().order_by('s_no')
    return render(request, "rti_HOD.html",{'HOD_details':HOD_details})

def rti_Tour_type(request):
    tour_type = RTI_Tour_type.objects.all().order_by('id')   
    return render(request, "rti_Tour_type.html", {'tour_type' : tour_type})


def rti_Tour_details(request, type_id):
    rti_type= get_object_or_404(RTI_Tour_type, id=type_id)
    tour_details = RTI_Tour_details.objects.filter(item=rti_type).order_by('-year')
    content = {"rti_type":rti_type, "tour_details":tour_details}
    return render(request, "rti_Tour_details.html", content)


def facility_to_Citizen(request):
    detail = Citizen.objects.all()
    return render(request, "facility_to_Citizen.html",{'detail':detail})


def Public_information_Officer(request):
    detail = Public_info_Officers.objects.all()
    return render(request, "PublicInfoOfficer.html",{'detail':detail})



  