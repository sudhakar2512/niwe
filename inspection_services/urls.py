from django.urls import path
from . import views

urlpatterns = [
    path('Inspection_menu/', views.Inspection_menu, name='Inspection_menu'),
    path('Inspection_Scope/', views.Inspection_Scope, name='/Inspection_Scope'),
    path('Inspection_procedure/', views.Inspection_procedure, name='/Inspection_procedure'),
    path('Inspection_Impartiality_policy/', views.Inspection_Impartiality_policy, name='/Inspection_Impartiality_policy'),
    path('Inspection_Complaints/', views.Inspection_Complaints, name='/Inspection_Complaints'),
 
]
