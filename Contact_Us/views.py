from django.shortcuts import render
from . models import ContactUs

def contact(request):
    contact = ContactUs.objects.all().order_by('id')
    if contact.exists():
        context = {'contact': contact}
        return render(request, "contact.html", context)
    return render(request, "contact.html")
