from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InNOut, Kfc, LittleCaesars, TacoBell
from .forms import NewUserForm

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Home Page View
def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

# InAndOut Page
def inAndOut(request):
    request.session.set_expiry(0)
    inAndOuts = InNOut.objects.all()
    ctx = {'inAndOuts':inAndOuts, 'active_link': 'inAndOut'}
    return render(request, 'food/inAndOut.html', ctx)

# LittleCaesars Page
def littleCaesars(request):
    request.session.set_expiry(0)
    littleCaesarss = LittleCaesars.objects.all()
    ctx = {'littleCaesarss':littleCaesarss, 'active_link': 'littleCaesars'}
    return render(request, 'food/littleCaesars.html', ctx)

# KFC Page
def kfc(request):
    request.session.set_expiry(0)
    kfcs = Kfc.objects.all()
    ctx = {'kfcs': kfcs, 'active_link': 'kfc'}
    return render(request, 'food/kfc.html', ctx)

# TacoBell Page
def tacoBell(request):
    request.session.set_expiry(0)
    tacoBells = TacoBell.objects.all()
    ctx = {'tacoBells': tacoBells, 'active_link': 'tacoBell'}
    return render(request, 'food/tacoBell.html', ctx)

# Order View Page
@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

# Order Success Page
def success(request):
    order = request.session['order']
    ctx = {'order': order}
    return render(request, 'food/success.html', ctx)

# Registration Page
def register(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'food/register.html', ctx)