from django.shortcuts import render
from django.http import HttpResponse
from .models import InNOut, Kfc, LittleCaesars, TacoBell
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Home Page View
def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

def inAndOut(request):
    request.session.set_expiry(0)
    inAndOuts = InNOut.objects.all()
    ctx = {'inAndOuts':inAndOuts, 'active_link': 'inAndOut'}
    return render(request, 'food/inAndOut.html', ctx)

def littleCaesars(request):
    request.session.set_expiry(0)
    littleCaesarss = LittleCaesars.objects.all()
    ctx = {'littleCaesarss':littleCaesarss, 'active_link': 'littleCaesars'}
    return render(request, 'food/littleCaesars.html', ctx)

def kfc(request):
    request.session.set_expiry(0)
    kfcs = Kfc.objects.all()
    ctx = {'kfcs': kfcs, 'active_link': 'kfc'}
    return render(request, 'food/kfc.html', ctx)

def tacoBell(request):
    request.session.set_expiry(0)
    tacoBells = TacoBell.objects.all()
    ctx = {'tacoBells': tacoBells, 'active_link': 'tacoBell'}
    return render(request, 'food/tacoBell.html', ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

def success(request):
    order = request.session['order']
    ctx = {'order': order}
    return render(request, 'food/success.html', ctx)