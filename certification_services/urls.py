from django.urls import path
from . import views

urlpatterns = [
    path('depart_certificate_menu/', views.depart_certificate_menu, name='depart_certificate_menu'),
    path('certificate_scheme/', views.certificate_scheme, name='/certificate_scheme'),
    path('certification_procedure/', views.certification_procedure, name='/certification_procedure'),
    path('department_certification_phc/', views.department_certification_phc, name='/department_certification_phc'),
    path('department_certification_roc/', views.department_certification_roc, name='/department_certification_roc'),
    path('department_certification_limitation/', views.department_certification_limitation, name='/department_certification_limitation'),
    path('department_certification_list/', views.department_certification_list, name='/department_certification_list'),
 
]
