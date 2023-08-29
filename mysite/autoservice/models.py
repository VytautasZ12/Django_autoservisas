from django.db import models


# Create your models here.
class AutomobilioModelis(models.Model):
    marke = models.CharField(verbose_name="Marke", max_length=100)
    modelis = models.CharField(verbose_name="Modelis", max_length=100)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilio modelis"


class Automobilis(models.Model):
    valst_nr = models.CharField(verbose_name="Valstybinis numeris", max_length=20)
    vin_kodas = models.CharField(verbose_name="VIN kodas", max_length=20)
    kliento_vardas = models.CharField(verbose_name="Klientas vardas", max_length=50)
    automobilio_modelis = models.ForeignKey(to="AutomobilioModelis", verbose_name="Modelis", on_delete=models.SET_NULL,
                                            null=True)

    def __str__(self):
        return f"{self.valst_nr} - {self.vin_kodas} ({self.automobilio_modelis}, {self.kliento_vardas})"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobilis"


class Uzsakymas(models.Model):
    data = models.DateField(verbose_name="Data", auto_now_add=True)
    automobilis = models.ForeignKey(to="Automobilis", verbose_name="Automobilis", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data}({self.automobilis})"

    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymas"


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.CASCADE)
    paslauga = models.ForeignKey(to="Paslauga", verbose_name="Paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField(verbose_name="Kiekis")

    def suma(self):
        return self.paslauga.kaina * self.kiekis

    def __str__(self):
        return f"{self.uzsakymas} ({self.paslauga} - {self.kiekis}: {self.suma()})"

    class Meta:
        verbose_name = "Uzsakymo eilute"
        verbose_name_plural = "Uzsakymo eilute"


class Paslauga(models.Model):
    pavadinimas = models.CharField(verbose_name="Paslaugos pavadinimas", max_length=50)
    kaina = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return f"{self.pavadinimas} ({self.kaina})"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"
