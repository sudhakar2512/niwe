from django.urls import path
from . import views

urlpatterns = [
    path('rti/', views.rti, name='rti'),
    path('rti/<int:info_id>', views.subInfo, name='subInfo'),

    path('audit_report/', views.audit_report, name='audit'), # RTI Audit report
    path('audit_report_description/<str:year>',views.audit_report_description,name='audit_report_description'), # RTI Audit report description

    path('annual_account/', views.annual_account, name='account'), # RTI Annual Account
    path('rti_governing_council', views.rti_governing_council, name='rti_governing_council'),    
    path('minutes_GC', views.minutes_GC, name='minutes_GC'),
    path('rti_application/', views.rti_application, name='rti_application'),
    path('rti_HOD/', views.rti_HOD, name='rti_HOD'),

    path('rti_Tour_type/', views.rti_Tour_type, name='rti_Tour_type'),      
    path('rti_Tour_type/<int:type_id>/', views.rti_Tour_details, name='rti_Tour_details'),    
    
    path('facility_to_Citizen/', views.facility_to_Citizen, name='facility_to_Citizen'),    
    path('Public_information_Officer/', views.Public_information_Officer, name='Public_information_Officer'),




]
