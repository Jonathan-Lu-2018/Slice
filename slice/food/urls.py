from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
    path('inAndOut', views.inAndOut, name='inAndOut'),
    path('littleCaesars', views.littleCaesars, name='littleCaesars'),
    path('kfc', views.kfc, name='kfc'),
    path('tacoBell', views.tacoBell, name='tacoBell')
]