from django.contrib import admin
from .models import back_plan


class back_plan1(back_plan):
    class Meta:
        proxy = True
        verbose_name = "添加回访计划"
        verbose_name_plural = "添加回访计划"


class back_plan_admin(admin.ModelAdmin):
    search_fields = ['back_customer']
    list_display = ['back_customer', 'back_state', 'back_data']
    fieldsets = (
        ('回访信息', {
            'fields': (
            'back_customer', 'back_data')}
         ),
    )
    readonly_fields = ['back_state']
    def save_model(self, request, obj, form, change):
        obj.service_phon = request.user.phone_number
        obj.save()
admin.site.register(back_plan1, back_plan_admin)
