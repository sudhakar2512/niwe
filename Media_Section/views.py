from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# 
def awards(request):
    award = Award.objects.all().order_by('id')
    if award.exists():
     return render(request, "awards.html", {'award':award})
# 
def events(request): 
    events = Events.objects.all().order_by('id')
    # if events.exists():
    context = {'events': events}
    return render(request, "events.html", context)



def media(request):
     return render(request, "media.html")

# 
def charterHeader(request):
    charter = Citizen_Charter.objects.first()
    if charter:
        return HttpResponse(charter.document_File.url)

# gallery/sub-gallery


def album_list(request): 
    albums = Gallery.objects.all().order_by('-album_id')
    return render(request, 'gallery.html', {'albums': albums})


def sub_album_list(request, album_id):
    album = get_object_or_404(Gallery, id=album_id)
    sub_albums = SubGallery.objects.filter(album=album).order_by('id')
    return render(request, 'sub_gallery.html', {'album': album, 'sub_albums': sub_albums})


def think_tank(request):
    albums = Think_Tank.objects.all().order_by('id')
    context={
        "albums" : albums
    }
    return render (request, "think-tank.html", context)

def sub_think_tank(request, think_id):
    album = get_object_or_404(Think_Tank, id=think_id)
    sub_albums = Sub_Think_Tank.objects.filter(album=album).order_by('id')
    return render(request, 'sub_think.html', {'album': album, 'sub_albums': sub_albums})

def global_windday_2022(request):
    windday_photo = windday_2022.objects.all()
    content = {"windday_photo":windday_photo}
    return render (request, "global_windday_2022_event.html", content)


def Pan_India_Meeting_2020(request):
    panindia_photo = panindia.objects.all()
    content = {"panindia_photo":panindia_photo}
    return render (request, "pan_india_meeting.html", content)


def global_RE_invest(request):
    global_invest_photo = global_invest.objects.all()
    content = {"global_invest_photo":global_invest_photo}
    return render (request, "global_RE_invest.html", content)



def training_solar_energy(request):
    solar_energy_photo = online_training_solar_energy.objects.all()
    content = {"solar_energy_photo":solar_energy_photo}
    return render (request, "training_solar_energy.html", content)