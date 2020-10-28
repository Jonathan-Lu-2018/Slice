from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home Page View
def index(request):
    return HttpResponse('Hello World!')

def pizza(request):
    return HttpResponse("I am pizza")