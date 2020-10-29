from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    order = Order.objects.all()
    return render(request, 'orders/wo.html', {'order': order})

def priceO(request):
    return render(request, 'orders/priceO.html')

def activeO(request):
    return render(request, 'orders/activeO.html')


def canceledO(request):
    return render(request, 'orders/canceledO.html')


def waitO(request):
    return render(request, 'orders/waitOh.html')


def doneO(request):
    return render(request, 'orders/doneO.html')

##сделать форму входа тут
