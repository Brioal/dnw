from django.contrib import admin

# Register your models here.
from organization.models import HeadStore, ProvinceAgent, CityAgent, LastStore
from users.models import MyUser


class HeadStore_Admin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    class Meta:
        model = HeadStore
class ProvinceAgent_Admin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "admin_user":
            kwargs["queryset"] = MyUser.objects.filter(admin_level=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    search_fields = ['name', 'parent__name']
    list_display = ['name', 'parent', 'admin_user']
    class Meta:
        model = ProvinceAgent
class CityAgent_Admin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "admin_user":
            kwargs["queryset"] = MyUser.objects.filter(admin_level=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    search_fields = ['name', 'parent__name']
    list_display = ['name', 'parent', 'admin_user']
    class Meta:
        model = CityAgent
class LastStore_Admin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "admin_user":
            kwargs["queryset"] = MyUser.objects.filter(admin_level=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    search_fields = ['name', 'parent__name']
    list_display = ['name', 'parent', 'admin_user']
    class Meta:
        model = LastStore

admin.site.register(HeadStore, HeadStore_Admin)
admin.site.register(ProvinceAgent, ProvinceAgent_Admin)
admin.site.register(CityAgent, CityAgent_Admin)
admin.site.register(LastStore, LastStore_Admin)


