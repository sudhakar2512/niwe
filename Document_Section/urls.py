from django.urls import path
from . import views

urlpatterns = [
    
    path('download/', views.download, name='document'),
    path('azadi_ka_amrit_mahotsav/', views.azadi_ka_amrit_mahotsav, name='amrit_mahotsav'),
    path('information_gi/', views.information_gi, name='GenInfo'),
    path('information_hwed/', views.information_hwed, name='hwed'),
    path('record_retention/', views.record_retention, name='retention'),
    # path('relatedlinks/', views.relatedlinks,name='related_links'),
    path('faq/', views.faq, name='faq'),
    path('power_policy', views.wind_power_policy, name='power_policy'),
    path('information_weg_installation/', views.information_weg_installation, name='information_weg_installation'),
    path('weg_install_country_wise/', views.weg_install_country_wise,name='weg_install_country_wise'),
    path('weg_install_India/', views.weg_install_India,name='weg_install_India'),

    path('event_schedule_22_23/', views.event_schedule_22_23, name='event_schedule_22_23'),
    path('report_detail_22_23/<int:event_id>/', views.report_detail_22_23, name='report_detail_22_23'),

    path('event_schedule_21_22/', views.event_schedule_21_22, name='event_schedule_21_22'),
    path('report_details_21_22/<int:event_id>', views.report_detail_21_22, name='report_detail_21_22'),
    

    

]

