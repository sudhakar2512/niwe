"""
URL configuration for NiwaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path#
    d a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django_otp.admin import OTPAdminSite

# 
import certification_services

admin.site.site_title = "NIWE WEBSITE - ADMINISTRATION"
admin.site.site_header = "NIWE WEBSITE MANAGEMENT"
admin.site.index_title = "NIWE DASHBOARD"

# For Enabling OTP authentication in niwe website admin page
admin.site.__class__= OTPAdminSite
urlpatterns = [
    
    
    # path('','admin_site_urls'),

    path('tinymce/', include('tinymce.urls')),
    path('', views.index),
        
    path('sitemap/', views.sitemap, name='sitemap'),
    path('screen-reader-access/', views.Screen_Reader, name='screen-reader-access'),
    # 
    path('about/', include('about_section.urls')),
    path('medias/', include('Media_Section.urls')),
    path('department/', include('Depart_Section.urls')),
    path('downloads/', include('Document_Section.urls')),
    path('Tenders/', include('Tenders.urls')),
    path('contact/', include('Contact_Us.urls')),
    path('dg_staff/', include('Staff_Section.urls')),
    path('', include('Right_To_Information.urls')),
    path('', include('certification_services.urls')),
    path('', include('inspection_services.urls')),    
    path('', include('search_form.urls')),    
    path('', include('home_sections.urls')),   
    path('careers/', include('Career_Section.urls')),
     
    path('department_srra_online_training/', views.department_srra_online_training, name='department_srra_online_training'),
    path('fowpi_workshop_presentation/', views.fowpi_workshop_presentation),
    path('fowpi_report/', views.fowpi_report),
   
    path('international_conference_wsra/', views.international_conference_wsra, name='international_conference_wsra'),
    path('international_workshop_ppt/', views.international_workshop_ppt, name='international_workshop_ppt'),
    
    path('ireda_niwe_annual_awards/', views.ireda_niwe_annual_awards, name='ireda_niwe_annual_awards'),
    path('ireda_niwe_annual_awards/<int:year>', views.ireda_niwe_annual_subawards, name='ireda_niwe_annual_subawards'),
    
    

    # path('media/', views.media),
    path('offshore_EPD_Gujarat/', views.offshore_EPD_Gujarat),
    path('offshore_lidar/', views.offshore_lidar),
    path('fowind_report/', views.fowind_report),
    path('pan-india_workshop/', views.pan_india_workshop, name='pan-india_workshop'),
    path('services/', views.services),
    path('small_wind_energy_&_hybrid_system_presentation/', views.small_wind_energy_hybrid_system_presentation, name='swe&hsp'),
    path('sub-gallery/', views.sub_gallery, name='sub-gallery'),
    path('tenders/', views.tenders),
    path('wind_potential/', views.wind_potential),
    path('disclaimer/', views.disclaimer),
    path('technical_reports/', views.technical_reports, name='technical_reports'),
    
    path('glossary/', views.glossery),

    # side tabs
    
    path('academy/', views.Academy),
    path('library/', views.Library),
      

    path('itec/', views.ITEC_training),
    path('itec_training/', views.ITEC_trainings, name='itec_training'),
    path('itec_training/<int:training_id>', views.ITEC_trainings_sub, name='itec_training_sub'),
    
    path('itec_countries/', views.ITEC_training_countries, name='itec_countries'),
    path('itec_feedback/', views.ITEC_training_feedback, name='itec_feedback'),
    #  
    path('newsletters', views.newsletters, name='newsletters'),
    path('news-letters/<str:issue>/', views.news_letter_reports_details, name='news_letter_reports_details'),

    path('annual_reports', views.annual_reports, name='annual_reports'),
    path('annual-reports/<str:year>/', views.annual_reports_details, name='annual_reports_details'),

    
    path('inter-national-trainings/', views.training_list, name='international_training_list'),
    path('inter-national-trainings/<slug:training_slug>/', views.eitec_detail, name='international_training_eitec'),
    path('inter-national-trainings/eitec/<slug:eitec_slug>/', views.sub_eitec_detail, name='international_training_sub_eite'),

    path('national-training/', views.national_training, name='national_training'),
    path('national-training/<slug:slug>/', views.national_training_data, name='national_training_data'),

    path('short_term_course/', views.short_term_course, name='short_term_course'),
    path('customize_training/', views.customize_training, name='customize_training'),
    path('customize_training/<int:id>', views.customize_training_sub, name='customize_sub_training'),

     path('training_calander/', views.training_calander, name='training_calander'),
     path('training_calander/<int:data_id>/', views.training_calander_sub, name='training_calander_sub'),
     
     path('global_wind_day/', views.global_wind_day, name='global_wind_day'),
     path('global_wind_day/<int:global_id>', views.gloabl_sub_wind_day, name='gloabl_sub_wind_day'),
     
     path('webinar/', views.webinar, name='webinar'),
     path('workshop_confrence/', views.workshop_confrence, name='workshop_confrence'),
     path('workshop_confrence/<int:workshop_id>/', views.workshop_confrence_images, name='workshop_confrence_year'),

     path('vayumitra_sdt/', views.vayumitra_sdt, name='vayumitra_sdt'),
    #  path('vayumitra_sdt/<int:vayumitra_id>', views.vayumitra_sdt_sub, name='vayumitra_sdt_sub'),
 
    path('events-updates', views.events_update, name='evnts_update'),
    path('whats-new-update', views.whatsNew, name='whatsNew_updates'),
   
    
    path('coorporate-film-hindi', views.corporate_film_hindi, name='corporate_film_hindi'),
    path('rfd/',views.rfd, name='rfd'),
    path('search/', views.search_results, name="search_results"),
    path('help_page/', views.help_page, name="help_page")
     
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ADMIN_ENABLED:
    # from django.contrib import admin
    urlpatterns += [path('admin/', admin.site.urls),]
    
