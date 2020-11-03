from django.shortcuts import render
from django.http import HttpResponse
from .models import InNOut, Kfc, LittleCaesars, TacoBell
# Create your views here.

# Home Page View
def index(request):
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

def inAndOut(request):
    inAndOuts = InNOut.objects.all()
    ctx = {'inAndOuts':inAndOuts, 'active_link': 'inAndOut'}
    return render(request, 'food/inAndOut.html', ctx)

def littleCaesars(request):
    littleCaesarss = LittleCaesars.objects.all()
    ctx = {'littleCaesarss':littleCaesarss, 'active_link': 'littleCaesars'}
    return render(request, 'food/littleCaesars.html', ctx)

def kfc(request):
    kfcs = Kfc.objects.all()
    ctx = {'kfcs': kfcs, 'active_link': 'kfc'}
    return render(request, 'food/kfc.html', ctx)

def tacoBell(request):
    tacoBells = TacoBell.objects.all()
    ctx = {'tacoBells': tacoBells, 'active_link': 'tacoBell'}
    return render(request, 'food/tacoBell.html', ctx)