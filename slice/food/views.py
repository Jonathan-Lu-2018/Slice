from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InNOut, Kfc, LittleCaesars, TacoBell, Order, Item
from .forms import NewUserForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import random
import json

def randomOrderNumber(length):
    sample = 'ABCDEFGH0123456789'
    numberOrder = ''.join((random.choice(sample) for i in range(length)))
    return numberOrder

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
        orders = json.loads(request.session['order'])
        request.session['bill'] = request.POST.get('bill')
        randomNum = randomOrderNumber(6)

        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            order = Order(customer=request.user, 
                            number=randomOrderNumber(6), 
                            bill=float(request.session['bill']), 
                            note=request.session['note'])
            order.save()
            request.session['orderNum'] = order.number
            for article in orders:
                item = Item(
                    order = order,
                    name = article[0],
                    price = float(article[1])
                )
                item.save()
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

# Order Success Page
def success(request):
    orderNum = request.session['orderNum']
    bill = request.session['bill']
    items = Item.objects.filter(order__number=orderNum)
    ctx = {'orderNum':orderNum, 'bill':bill, "items":items}
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

# Login page
def logIn(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'The login information is invalid')
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')