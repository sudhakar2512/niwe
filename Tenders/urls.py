
from django.urls import path
from . import views

urlpatterns = [
    path('tender_data/', views.tender_data, name='tender_data'),
    path('tenders/archived/', views.archived_tenders, name='archived-tenders'),
    
    path('Purchase_order_list/', views.Purchase_order_list, name='Purchase_order_list'),
    path('Purchase_order_list/archived/', views.archived_Purchase_order_list, name='archived_Purchase_order_list'),
]