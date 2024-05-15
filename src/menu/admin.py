from django.contrib import admin
from .models import RegularPizza, SicilianPizza

class RegularPizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('name',)
    ordering = ('id',)

class SicilianPizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('name',)
    ordering = ('id',)

admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
# Other model registrations
