from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('events/', views.events, name='events'),
    path('events/', views.events, name='events'),
    path('charter/', views.charterHeader, name='citizen'),
    path('media/', views.media, name='medias'),
    path('awards/', views.awards, name='awards'),
    path('gallery/', views.album_list, name='gallery'),
    path('gallery/<int:album_id>/', views.sub_album_list, name='sub_gallery'),
    
    path('think_tank/', views.think_tank, name='think_tank'),
    path('think_tank/<int:think_id>', views.sub_think_tank, name='sub_think_tank'),
    path('global_windday_2022/', views.global_windday_2022, name='global_windday_2022'),    
    path('Pan_India_Meeting_2020/', views.Pan_India_Meeting_2020, name='Pan_India_Meeting_2020'),
    path('global_RE_invest/', views.global_RE_invest, name='global_RE_invest'),
    path('training_solar_energy/', views.training_solar_energy, name='training_solar_energy'),
   
]

