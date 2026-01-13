# from home_sections.models import VisitorCount
# from django.http import HttpResponse, request


# def visitor_count(request):
#     try:
#         count_obj = VisitorCount.objects.first()
#         visitor_count_value = count_obj.count if count_obj else 0
#     except VisitorCount.DoesNotExist:
#         visitor_count_value = 0
#     return {'visitor_count': visitor_count_value}

from home_sections.models import VisitorCount, WebsiteLastUpdate
from django.http import HttpResponse, request


def footer_details(request):
    try:
        count_obj = VisitorCount.objects.first()
        visitor_count_value = count_obj.count if count_obj else 0
    except VisitorCount.DoesNotExist:
        visitor_count_value = 0

    try:
        update_info = WebsiteLastUpdate.objects.first()
    except WebsiteLastUpdate.DoesNotExist:
        update_info = None

    return {
        'visitor_count': visitor_count_value,
        'update_info': update_info
    }