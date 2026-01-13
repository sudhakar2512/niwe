from django.shortcuts import render
from django.http import request

# Create your views here.

def Inspection_menu(request):
    
      return render(request, 'Inspection_menu.html')


def Inspection_Scope(request):
      return render(request, 'Inspection_Scope.html')


def Inspection_procedure(request):
      return render (request, 'Inspection_procedure.html')


def Inspection_Impartiality_policy(request):
      return render(request, 'Inspection_Impartiality_policy.html')


def Inspection_Complaints(request):
      return render (request, 'Inspection_Complaints.html')
