from django.urls import path
from . import views

urlpatterns = [

    path('about_background/', views.about_background, name='background'),
    path('about_charter/', views.about_charter, name='charter'),
    path('about_dgm/', views.about_dgm, name='dgm'),
    path('about_org/', views.about_org, name='org'),
    path('about_qlty_ply/', views.about_qlty_ply, name='quality'),
    path('about_us/', views.about_us, name='us'),
]