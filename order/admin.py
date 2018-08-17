from django.contrib import admin

# Register your models here.
from order.models import Discount


class discountAdmin(admin.ModelAdmin):
    search_fields = ['discount']
    list_display = ['discount']

admin.site.register(Discount, discountAdmin)