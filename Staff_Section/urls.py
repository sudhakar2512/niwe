from django.urls import path
from . import views

urlpatterns = [
    
    # 
    path('director_general_staff/', views.about_staff, name='dg_staff'),
    path('director_general_staff/<int:dgStaff_id>/', views.about_staff_photo, name='dg_staff_photo'),
    
    path('staff_profile_cert/', views.staff_profile_cert, name='staff_cert'),
    path('staff_profile_cert/<int:certStaff_id>/', views.Certification_Staff_Photo, name='cert_staff_photo'),
    
    path('staff_profile_fa/', views.staff_profile_fa, name='staff_fin'),
    path('staff_profile_fa/<int:finance_id>/', views.finance_staff_photo, name='finance_staff_photo'),

    path('staff_profile_rnd/', views.staff_profile_rnd, name='staff_rnd'),
    path('staff_profile_rnd/<int:rnd_id>/', views.rnd_staff_photo, name='rnd_staff_photo'),

    path('staff_profile_sdt/', views.staff_profile_sdt, name='staff_sdt'),
    path('staff_profile_sdt/<int:sdt_id>/', views.sdt_staff_photo, name='sdt_staff_photo'),

    path('staff_profile_snr/', views.staff_profile_snr, name='staff_snr'),
    path('staff_profile_snr/<int:snr_id>/', views.snr_staff_photo, name='snr_staff_photo'),

    path('staff_profile_wra/', views.staff_profile_wra, name='staff_wra'),
    path('staff_profile_wra/<int:wra_id>/', views.wra_staff_photo, name='wra_staff_photo'),

    path('staff_profile_owd/', views.staff_profile_owd, name="staff_owd"),
    path('staff_profile_owd/<int:owd_id>/', views.owd_staff_photo, name='owd_staff_photo'),

    path('staff_profile_testing/', views.staff_profile_testing, name="staff_testing"),
    path('staff_profile_testing/<int:testing_id>/', views.testing_staff_photo, name='testing_staff_photo'),


]
