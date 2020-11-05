from django.contrib import admin
from .models import InNOut, Kfc, LittleCaesars, TacoBell, Order, Item

# InNOut Admin
class InNOutAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(InNOut, InNOutAdmin)

# Kfc Admin
class KfcAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(Kfc, KfcAdmin)

# LittleCasearsAdmin
class LittleCaesarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(LittleCaesars, LittleCaesarsAdmin)

# TacoBell Admin
class TacoBellAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(TacoBell, TacoBellAdmin)

admin.site.register(Order)
admin.site.register(Item)