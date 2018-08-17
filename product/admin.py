from django.contrib import admin
from .models import Product, Instrument


# Register your models here.

#产品录入

class productAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'number']

admin.site.register(Product, productAdmin)

class instrumentAdmin(admin.ModelAdmin):
     search_fields = ['name']
     list_display = ['name']
admin.site.register(Instrument, instrumentAdmin)