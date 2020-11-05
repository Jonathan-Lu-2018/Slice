from django.db import models
from django.contrib.auth.models import User

# InNOut model
class InNOut(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    inNOutImage = models.URLField()

# Kfc model
class Kfc(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    kfcImage = models.URLField()

# LittleCaesars model
class LittleCaesars(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    littleCaesarsImage = models.URLField()

# TacoBell model
class TacoBell(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    tacoBellImage = models.URLField()

# Order model
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=60)
    bill = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    note = models.TextField(blank=True, null=True)

# Item model linking to order
class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=60)