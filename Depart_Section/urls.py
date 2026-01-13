from django.urls import path
from . import views

urlpatterns = [
    
    path('depart_side_tabs/', views.depart_side_tabs, name='sideTab'),
    path('department_certification/', views.department_certification, name='certificate'),
    
    path('department_tsnr_menu/', views.department_tsnr_menu, name='testing_snr'),
    
    path('department_fa/', views.department_fa, name='finance'),
    path('department_fna_admin/', views.department_fna_admin, name='admin'),
    path('department_fna_finance/', views.department_fna_finance, name='fin'),
    path('department_fna_purchase/', views.department_fna_purchase, name='purchase'),
    
    path('department_owd_lidar_raw_data/', views.department_owd_lidar_raw_data, name='rawData'),
    path('department_owd/', views.department_owd, name='owd'),
    path('department_rnd/', views.department_rnd, name='r&d'),
    # 
    path('department_testing_menu/', views.department_testing_menu, name='testing_menu'),
    path('department_s&r/', views.department_snr, name='s&d'),

    path('testing_station_photo/', views.testing_station_photo, name='testing_station_photo'),
    path('testing_documents/', views.testing_documents, name='testing_documents'),
    path('depart_test_measure/', views.depart_test_measure, name='depart_test_measure'),
    path('depart_test_measure/<int:test_id>/', views.depart_test_type, name='depart_test_type'),
    
    # path('depart_turbine/', views.depart_turbine, name='depart_turbine'),
    
    #  
    path('department_sdt/', views.department_sdt, name='sdt'),
    path('department_srra_brief_report/', views.department_srra_brief_report, name='report'),
    path('department_srra_online_training/', views.department_srra_online_training, name='training'),
    # 
    path('department_wra/', views.department_wra, name='wra'),
    path('department_wra_swms', views.wind_monitor_status, name='wra_status'),
    path('department_wra_ps', views.wind_sale, name='wra_sale'),
    path('department_wra_ssra_stations', views.wra_srra_station, name='wra_srra_station'),
    path('department_wra_station_map', views.wra_station_map, name='wra_station_map'),
    
    path('department_wra-phase/', views.wra_srra_phases, name='wra_srra_phases'),
    path('department_wra-phaseII/', views.wra_srra_phaseII, name='wra_srra_phaseII'),
    path('department_wra-stations-meda/', views.wra_srra_phase_meda, name='wra_srra_station_meda'),
    path('department_wra-stations-anert/', views.wra_srra_phase_anert, name='wra_srra_station_anert'),
    path('department_wra-stations-ams/', views.wra_srra_phase_ams, name='wra_srra_station_ams'),

    path('department_wra-msr/', views.wra_micro_servey, name='wra_micro_servey'),
    path('department_wra-numwind/', views.wra_numerical_wind, name='wra_numerical_wind'),
    path('department_wra-wpd/', views.wra_wpd_map, name='wra_wpd_map'),
    path('department_wra-power-estimate/', views.wra_wind_power_estimate, name='wra_power_estimate'),

    path('department_wra&o_fowind_report/', views.department_wrao_fowind_report, name='wra&o'),
    path('department_wra&o_offshore_portal/', views.department_wrao_offshore_portal, name='portal'),
    path('departments/', views.departments, name='departments'),
    path('department_wra_wps/', views.wind_potential_sites, name='wind_potential_sites'),
]
