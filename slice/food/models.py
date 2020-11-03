from django.db import models

# InNOut model
class InNOut(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    inNOutImage = models.URLField()

class Kfc(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    kfcImage = models.URLField()

class LittleCaesars(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    littleCaesarsImage = models.URLField()

class TacoBell(models.Model):
    name   = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=4, decimal_places=2)
    tacoBellImage = models.URLField()