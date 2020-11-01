from django.contrib import admin
from .models import InNOut, Kfc, LittleCaesars, TacoBell

# InNOut Admin
class InNOutAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(InNOut, InNOutAdmin)

class KfcAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(Kfc, KfcAdmin)

class LittleCaesarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(LittleCaesars, LittleCaesarsAdmin)

class TacoBellAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(TacoBell, TacoBellAdmin)