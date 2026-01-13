from django.utils.translation import get_language
from django.core.paginator import Paginator

from django.shortcuts import render
from . models import *
from django.db.models import Prefetch



def related_links(request):
    related_links =Related_links.objects.all().order_by('id')
    context={
        "related_links" : related_links
    }
    
    return render(request, "relatedlinks1.html", context)


def website_policy(request):
    return render (request, "web-policy.html")

def WebInformationManager(request):
    return render (request, "WebInformationManager.html")

def apprenticeship_training(request):
    return render(request,"apprenticeship-training.html")

def windSolar_saleDate(request):
    return render (request,"windSolar-Saledate.html")

def mnre_updates_full_view(request):
    mnre_full_view = MNRE_WhatsNew.objects.filter(is_archived=False).order_by('id')
    paginator = Paginator(mnre_full_view, 10)  # Show 10 entries per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the entries for the current page
    
    context = {
        "mnre_full_view": page_obj,
        "page_obj": page_obj,
    }

    return render(request,"mnre_whatsnew_full_view.html", context)

def MNRE_archived_WhatsNew(request):
    archived_items = MNRE_WhatsNew.objects.filter(is_archived=True).order_by('-archived_at')    
    paginator = Paginator(archived_items, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'MNRE_archived_WhatsNew.html', {'page_obj': page_obj})  

def Events_full_view(request):
    events_full_view = Events_New.objects.all().order_by('-id')
    paginator = Paginator(events_full_view, 10)  # Show 10 entries per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the entries for the current page
    context = {
        "events_full_view": page_obj,
        "page_obj" : page_obj,}
    
    return render(request,"Events_full_view.html", context)

def Whatsnew_full_view(request):
    
    ordered_corrigenda = WhatsNewCorrigendum.objects.order_by('id')

    # Main queryset with prefetching
    whatsnew_items = WhatsNew.objects.prefetch_related(
        Prefetch('corrigendam', queryset=ordered_corrigenda)
    ).filter(is_archived=False).order_by('-id')

    paginator = Paginator(whatsnew_items, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Whatsnew_full_view.html', {'page_obj': page_obj})


def archived_WhatsNew(request):
    archived_items = WhatsNew.objects.filter(is_archived=True).order_by('-archived_at')    
    paginator = Paginator(archived_items, 15)  # Show 15 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'archived_WhatsNew.html', {'page_obj': page_obj}) 

def Running_news_full_view (request):
    runningnews_full_view = Running_News.objects.all().order_by('-id')  # Fetch all entries
    paginator = Paginator(runningnews_full_view, 10)  # Show 10 entries per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the entries for the current page

    context = {
        "runningnews_full_view": page_obj,  # Paginated data
        "page_obj": page_obj,  # Paginated data
    }
    return render(request, "Running_news_full_view.html", context)
