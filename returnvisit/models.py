from django.db import models
from store.models import Customer
#客户回访
class back_plan(models.Model):
    #回访日期
    back_data = models.DateField(verbose_name="回访日期", null=True, blank=True)
    #回访状态
    back_state = models.BooleanField(default=False, verbose_name="回访状态")
    #回访客户
    back_customer = models.ForeignKey(Customer, verbose_name="客户姓名",  related_name='customer_name',  on_delete=models.DO_NOTHING, null=True, blank=True)
    #客服电话
    service_phon = models.CharField(verbose_name='手机号', max_length=255)
    class Meta:
        verbose_name = "客户回访"
        verbose_name_plural = "客户回访"