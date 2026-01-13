from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from Tenders.models import *
from django.core.paginator import Paginator
from django.db.models import Prefetch


def tender_data(request):
    # Order corrigenda by ID descending (or change to 'title', etc.)
    ordered_corrigenda = Corrigendum.objects.order_by('id')

    tenders = TenderPage.objects.prefetch_related(
        Prefetch('corrigenda', queryset=ordered_corrigenda)
    ).filter(is_archived=False).order_by('-id')

    paginator = Paginator(tenders, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tenders.html', {'page_obj': page_obj})

# def tender_data(request):   
#     tenders = TenderPage.objects.prefetch_related('corrigenda') \
#                                 .filter(is_archived=False) \
#                                 .order_by('-id')   
#     paginator = Paginator(tenders, 15)  # Show 15 items per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'tenders.html', {'page_obj': page_obj})


def archived_tenders(request):
    archived_items = TenderPage.objects.filter(is_archived=True).order_by('-archived_at')
    
    paginator = Paginator(archived_items, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'archived_tenders.html', {'page_obj': page_obj})


def Purchase_order_list(request):
    items = PurchaseOrder.objects.filter(is_archived=False).order_by('-id')
    
    paginator = Paginator(items, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Purchase_orders.html', {'page_obj': page_obj})


def archived_Purchase_order_list(request):
    archived_items = PurchaseOrder.objects.filter(is_archived=True).order_by('-archived_at')
    
    paginator = Paginator(archived_items, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'archived_Purchase_orders.html', {'page_obj': page_obj})