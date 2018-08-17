import datetime

from django.contrib import admin

# Register your models here.
from store.models import Customer
from users.models import MyUser

#网络客服
class Customer_ADMIN(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['state', 'name', 'phone', 'order_time', 'web_staff','register_time', 'arrive_time', 'store']
    #
    fieldsets = (
        ('客户基本信息', {

                         'fields': ('name', 'phone', 'phone1', 'qq_num', 'we_num', 'birthday', 'constellation', 'channel', 'client', 'sex', 'age', 'area', 'store', 'order_num', 'order_time', 'note')}

        ),
    )
    class Meta:
        model = Customer

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "web_staff":
            kwargs["queryset"] = MyUser.objects.filter(job=2)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        if request.user.job == 2:
            obj.web_staff = request.user
        obj.register_time = datetime.datetime.now()
        super().save_model(request, obj, form, change)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        web_staff = request.user.id

        if(request.user.job == 1 or request.user.job == 0):
            return qs.filter(is_from_web=True)
        else:
            return qs.filter(is_from_web=True).filter(web_staff=web_staff)


admin.site.register(Customer, Customer_ADMIN)
#前台
class Customer2(Customer):
    class Meta:
        proxy = True
        verbose_name = "客户信息_前台"
        verbose_name_plural = "客户信息_前台"


class Customer_ADMIN2(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'state', 'web_staff']
    fieldsets = (
        ('客户信息', {
            'fields': ('name', 'phone', 'phone1', 'qq_num', 'we_num', 'birthday', 'constellation', 'channel', 'client', 'sex', 'age', 'area', 'store', 'front_staff', 'beauty_consultant', 'order_num', 'order_time', 'register_time', 'note')}
         ),
    )
    class Media:
        css = {
            # "all": ("my_styles.css",)
        }
        js = ("vin_search/jquery.js", "vin_search/test.js", )

    readonly_fields = ()

    class Meta:
        model = Customer



    def save_model(self, request, obj, form, change):
        # if obj.beauty_consultant is not None:
        #     obj.state = 1
        if obj.state == 0:
            obj.state = 1
            obj.arrive_time = datetime.datetime.now()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        admin_user = request.user
        if(request.user.admin_level == 2):
            admin_user = MyUser.objects.get(id = request.user.parent_id)
        return qs.filter(store=admin_user.user_org2.get())


    #根据是否是网络客服预约来进行不同字段的显示
    def get_readonly_fields(self, request, Customer = None):
        if Customer is None:
            temp_fields=()
            self.readonly_fields = temp_fields
            print(self.readonly_fields)
        else:
            temp1_fields=('name', 'phone', 'store', 'web_staff')
            self.readonly_fields=temp1_fields
        return self.readonly_fields

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        admin_user = request.user
        if (request.user.admin_level == 2):
            admin_user = MyUser.objects.get(id=request.user.parent_id)
        if db_field.name == "front_staff":
            kwargs["queryset"] = MyUser.objects.filter(job=3).filter(parent_id=admin_user.id)
        if db_field.name == "beauty_consultant":
            kwargs["queryset"] = MyUser.objects.filter(job=4).filter(parent_id=admin_user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Customer2, Customer_ADMIN2)

# 回访设置
class Customer3(Customer):
    class Meta:
        proxy = True
        verbose_name = "设置客户回访"
        verbose_name_plural = "设置客户回访"

class Customer_ADMIN3(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'back_date', 'back_note']
    fieldsets = (
        ('客户信息', {
            'fields': (
            'name', 'phone', 'back_date', 'back_note')}
         ),
    )
    readonly_fields = ('name', 'phone', )

    class Meta:
        model = Customer

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        admin_user = request.user
        if(request.user.admin_level == 2):
            admin_user = MyUser.objects.get(id = request.user.parent_id)
        return qs.filter(store=admin_user.user_org2.get())

admin.site.register(Customer3, Customer_ADMIN3)
# 今日所需回访
class Customer4(Customer):
    class Meta:
        proxy = True
        verbose_name = "今日所需回访"
        verbose_name_plural = "今日所需回访"

class Customer_ADMIN4(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'back_date', 'back_note']
    fieldsets = (
        ('客户信息', {
            'fields': (
            'name', 'phone', 'back_date', 'back_note')}
         ),
    )
    readonly_fields = ('name', 'phone', 'back_date', 'back_note')

    class Meta:
        model = Customer

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        admin_user = request.user
        if(request.user.admin_level == 2):
            admin_user = MyUser.objects.get(id = request.user.parent_id)
        return qs.filter(store=admin_user.user_org2.get()).filter(back_date=datetime.datetime.now())

admin.site.register(Customer4, Customer_ADMIN4)

# 客户信息_咨询师
class Customer5(Customer):
    class Meta:
        proxy = True
        verbose_name = "客户信息_咨询师"
        verbose_name_plural = "客户信息_咨询师"

class Customer_ADMIN5(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', ]
    fieldsets = (
        ('客户信息', {
            'fields': (
            'name', 'phone','phone1', 'qq_num', 'sex', 'age', 'area', 'store', 'front_staff', 'ill_place', 'ill_time', 'ill_kind', 'note')}
         ),
    )
    readonly_fields = ('name', 'phone', 'store', 'front_staff')

    class Meta:
        model = Customer

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        admin_user = request.user
        if (request.user.admin_level == 2):
            admin_user = MyUser.objects.get(id=request.user.parent_id)
        return qs.filter(store=admin_user.user_org2.get()).filter(beauty_consultant=request.user)

admin.site.register(Customer5, Customer_ADMIN5)