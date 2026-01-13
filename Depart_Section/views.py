from django.shortcuts import render, get_object_or_404
from django.http import request
from . models import *
from . models import Reserach_n_Development, Testing_and_Standards_Regulation, Departments, Wind_Resources_Assessment, Finance_and_Administration, Offshore_Wind_Development, Skill_developements_training


def depart_side_tabs(request):
    return render(request, "depart-side-tabs.html")


def department_certification(request):
    return render(request, "department_certification.html")

def department_tsnr_menu(request):
    return render(request, "department_tsnr_menu.html")

def department_fa(request):

    fin = Finance_and_Administration.objects.all()
    if fin.exists():
        context = {"fin": fin}
    return render(request, "department_fa.html", context)


def department_fna_admin(request):
    return render(request, "department_fna_admin.html")


def department_fna_finance(request):
    Finance=Department_Fna_Finance.objects.all().order_by('id')
    context={
        "Finance":Finance
    }
    return render(request, "department_fna_finance.html", context)


def department_fna_purchase(request):
    purchase = Department_Fna_Purchase.objects.all()
    context={
        "purchase":purchase
    }
    return render(request, "department_fna_purchase.html", context)


def department_owd_lidar_raw_data(request):
    return render(request, "department_owd_lidar_raw_data.html")


# owd
def department_owd(request):
    owd = Offshore_Wind_Development.objects.all()
    context = {"owd": owd}
    return render(request, "department_owd.html", context)

    
# rnd
def department_rnd(request):
    RnD = Reserach_n_Development.objects.all().order_by('id')
    # if RnD.exists():
    content = {'RnD': RnD}
    return render(request, "department_rnd.html", content)        


# sdt
def department_sdt(request):
    sdt_list = Skill_developements_training.objects.all().order_by('id')
    # if sdt_list.exists():
    context = {'Sdt': sdt_list}
    return render(request, "department_sdt.html", context)


# snr
def department_snr(request):
    snr = Testing_and_Standards_Regulation.objects.all().order_by('id')
    print(snr)
    # if snr.exists():
    content = {'snr': snr}
    return render(request, "department_s&r.html", content)
    # else: 
        # return render(request, "department_s&r.html")

# 

def department_testing_menu(request):
    testing = Testing_menu.objects.all()
    print(testing)
    # if snr.exists():
    content = {'testing': testing}
    return render(request, "department_testing.html", content)
    # else: 
        # return render(request, "department_s&r.html")

# 

def testing_station_photo(request):
    terbine_photo = Wind_Terbine_photo.objects.all()
    content = {"terbine_photo":terbine_photo}
    return render (request, "depart_wind_terbine_photo.html", content)


def testing_documents(request):
    document = depart_documents.objects.all()
    content = {"document": document}
    return render(request, "depart_documents.html", content)


def depart_test_measure(request):
    depart = Department_testing_measure.objects.all()
    content = {"depart":depart}
    return render(request, "depart_test_measure.html", content)


def depart_test_type(request, test_id):
    item = get_object_or_404(Department_testing_measure, id=test_id)
    depart_type = Department_testing_measureType.objects.filter(item=item).order_by('id')
    content = {"item": item, "depart_type":depart_type}
    return render(request, "depart_test_measure_type.html", content)

# def depart_turbine(request):
#     return render(request, "depart_wind_turbine.html")

    
# 
def department_srra_brief_report(request):
    return render(request, "department_srra_brief_report.html")


# 
def department_srra_online_training(request):
    return render(request, "department_srra_online_training.html")


# wra
def department_wra(request):
    sdt_list = Wind_Resources_Assessment.objects.all().order_by('id')
    # if sdt_list.exists():
    context = {'wra': sdt_list}
    return render(request, "department_wra.html", context)


def wind_monitor_status(request):
    return render (request, 'department_wra_status_wind.html')


def wind_sale(request):
    wra_sale = WRA_Sale_publication.objects.all().order_by('id')
    context = {"wra_sale": wra_sale} 
    return render (request, 'department_wra_sale.html', context)


def wra_srra_station(request):
    wra_station = WRA_srra_stations.objects.all()
    context = {"wra_station": wra_station}
    return render (request, 'department_wra_station.html', context)


def wra_wind_power_estimate(request):
    power = WRA_Estimated_Potential.objects.all().order_by('id')
    context = {"power": power}
    return render (request, 'department_wra_wind_power_estimation.html',context)


def wra_srra_phases(request):
    station = WRA_Srra_Station_phases.objects.order_by('id')
    context = {"station": station}
    return render (request, 'department_wra_srra_phase.html',context)

def wra_srra_phaseII(request):
    station = WRA_Srra_Station_phaseII.objects.order_by('id')
    context = {"station": station}
    return render (request, 'department_wra_srra_phaseII.html',context)

def wra_srra_phase_meda(request):
    station = WRA_Srra_Station_meda.objects.order_by('id')
    context = {"station": station}
    return render (request, 'department_wra_srra_stations_meda.html',context)

    
def wra_srra_phase_anert(request):
    station = WRA_Srra_Station_anert.objects.order_by('id')
    context = {"station": station}
    return render (request, 'department_wra_srra_stations_anert.html', context)

    
def wra_srra_phase_ams(request):
    station = WRA_Srra_Station_ams.objects.order_by('id')
    context = {"station": station}
    return render (request, 'department_wra_srra_stations_ams.html', context)


def wra_station_map(request):
    return render (request, 'department_wra_station_map.html',)


# 
def wra_micro_servey(request):
    servey = WRA_Micro_Servey.objects.all()
    context = {
        "servey": servey
    }
    return render (request, 'department_wra_micro_servo.html', context)


# 
def wra_wpd_map(request):
    return render (request, 'department_wra_wpd_map.html',)


# 
def wra_numerical_wind(request):
    num_wind = WRA_Numeric_Wind.objects.all()
    context = {
        "num_wind": num_wind
    }
    return render (request, 'department_wra_numerical_wind.html', context)
# 


# 
def department_wrao_fowind_report(request):
    return render(request, "department_wra&o_fowind_report.html")


# 
def department_wrao_offshore_portal(request):
    return render(request, "department_wra&o_offshore_portal.html")


# 
def departments(request):

    depart = Departments.objects.all().order_by('id')
    # if depart.exists():
    context = {'depart': depart}
    return render(request, "departments.html", context)

# 
def wind_potential_sites(request):
    sites = WindPotentialSite.objects.all()  # Get all records
    return render(request, 'wind_potential_sites.html', {'sites': sites})
