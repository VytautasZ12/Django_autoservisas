from django.db import models


# Create your models here.
class AutomobilioModelis(models.Model):
    marke = models.CharField(verbose_name="Marke", max_length=100)
    modelis = models.CharField(verbose_name="Automobilio modelis", max_length=100)


class Automobilis(models.Model):
    valst_nr = models.CharField(verbose_name="Valstybinis numeris", max_length=20)
    vin_kodas = models.CharField(verbose_name="VIN kodas", max_length=20)
    kliento_vardas = models.CharField(verbose_name="Klientas vardas", max_length=50)
