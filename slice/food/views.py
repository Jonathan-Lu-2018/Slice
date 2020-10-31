from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home Page View
def index(request):
    return render(request, 'food/index.html')

def inAndOut(request):
    return render(request, 'food/inAndOut.html')

def littleCaesars(request):
    return render(request, 'food/littleCaesars.html')

def pandaExpress(request):
    return render(request, 'food/pandaExpress.html')

def tacoBell(request):
    return render(request, 'food/tacoBell.html')