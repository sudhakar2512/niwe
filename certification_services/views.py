from django.shortcuts import render
from django.http import request
from . models import Certification_Procedure

# Create your views here.

def depart_certificate_menu(request):
    
      return render(request, 'department_certification_menu.html')


def certificate_scheme(request):
      return render(request, 'certificate_scheme.html')

#  info = GeneralInformation.objects.all().order_by('id')
#     if info.exists():
      #   context = {'info': info}


def certification_procedure(request):
      info = Certification_Procedure.objects.all().order_by('id')
      if info.exists():
        context = {'info': info}
        return render (request, 'certification_procedure.html',context)      
      return render (request, 'certification_procedure.html')


def department_certification_phc(request):
      return render(request, 'department_certification_phc.html')


def department_certification_roc(request):
      return render (request, 'department_certification_roc.html')


def department_certification_limitation(request):
      return render (request, 'department_certification_limitation.html')


def department_certification_list(request):
      return render (request, 'department_certification_list.html')

