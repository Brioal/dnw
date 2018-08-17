from django.contrib import admin

# Register your models here.
from indexpage.models import Notice


class Notice_Admin(admin.ModelAdmin):
    list_display = ['message']
    class Meta:
        model = Notice

admin.site.register(Notice, Notice_Admin)