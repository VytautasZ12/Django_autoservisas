from django.contrib import admin
from .models import AutomobilioModelis, Automobilis, Uzsakymas, UzsakymoEilute, Paslauga


class AutomobilioModelisAdmin(admin.ModelAdmin):
    list_display = ["marke", "modelis"]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ["kliento_vardas", "automobilio_modelis", "valst_nr", "vin_kodas"]
    list_filter = ["kliento_vardas", "automobilio_modelis__marke", "automobilio_modelis__modelis"]
    search_fields = ["valst_nr", "vin_kodas"]


class UzsakymasInLIne(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ["data", "automobilis"]
    inlines = [UzsakymasInLIne]


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ["pavadinimas", "kaina"]


# Register your models here.
admin.site.register(AutomobilioModelis, AutomobilioModelisAdmin)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)
admin.site.register(Paslauga, PaslaugaAdmin)
