from django.conf.urls.i18n import i18n_patterns

from django.urls import path
from . import views

# urlpatterns = i18n_patterns(
urlpatterns = (
    
    path('related-links/', views.related_links, name='related_links'),
    path('web-policy/', views.website_policy, name='web_ploicy'),
    
    path('apprenticeship-trainig/', views.apprenticeship_training, name="apprenticeship_training"),
    path('windsolar-date-Sale/', views.windSolar_saleDate, name="windSolar_DateSale"),
  
    path('WebInformationManager/', views.WebInformationManager, name='WebInformationManager'),

    path('mnre_updates_full_view/', views.mnre_updates_full_view, name='mnre_updates_full_view'),  
    path('MNRE_archived_WhatsNew/', views.MNRE_archived_WhatsNew, name='MNRE_archived_WhatsNew'),   
    path('Events_full_view/', views.Events_full_view, name='Events_full_view'),
    path('Whatsnew_full_view/', views.Whatsnew_full_view, name='Whatsnew_full_view'),
    path('archived_WhatsNew/', views.archived_WhatsNew, name='archived_WhatsNew'),
    path('Running_news_full_view/',views.Running_news_full_view, name='Running_news_full_view'),
    
)