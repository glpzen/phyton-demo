from django.shortcuts import render
from demo.models import Vehicle
from django.http import JsonResponse
import datetime
from django.db.models import F


def show(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=2)
    vehicles = Vehicle.objects.order_by("-records__datetime").filter(records__datetime__gte=date_from).annotate(
        latitude=F('records__latitude'), longitude=F('records__longitude'), vehicle_plate=F('plate'),
        datetime=F('records__datetime')).values('latitude', 'longitude', 'vehicle_plate', 'datetime')
    return JsonResponse(list(vehicles), safe=False)
