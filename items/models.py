from django.db import models

#项目表
from product.models import Product, Instrument


class Item(models.Model):
    #项目名
    item_name = models.CharField(max_length=30, verbose_name="项目名", null=True)
    #价格
    item_price = models.IntegerField(verbose_name = '价格', null=True)
    #次数
    frequency = models.IntegerField(verbose_name = '次数', null=True)
    #类别
    classify = models.CharField(max_length=30, verbose_name="项目类别", null=True)
    def __str__(self):
        return self.item_name
#步骤
class Step(models.Model):
    #所属项目
    belong_item = models.ForeignKey(Item, verbose_name="所属项目", on_delete=models.DO_NOTHING, null=True)
    #第n步
    step_num = models.IntegerField(verbose_name='序号', null=True)
    #步骤内容
    step_content = models.CharField(max_length=1000, null=True)


#项目_产品表
class Item_Product(models.Model):
    #所属项目
    item = models.ForeignKey(Item, verbose_name="所属项目", on_delete=models.DO_NOTHING, null=True)
    #产品
    product = models.ForeignKey(Product, verbose_name="产品", on_delete=models.DO_NOTHING, null=True)
    #第n步
    step = models.IntegerField(verbose_name='序号', null=True)
    #数量
    num = models.IntegerField(verbose_name='数量', null=True)
    #用时
    time = models.IntegerField(verbose_name='用时', null=True)


#项目_仪器表
class Item_Instrument(models.Model):
    #所属项目
    item = models.ForeignKey(Item, verbose_name="所属项目", on_delete=models.DO_NOTHING, null=True)
    #仪器
    instrument = models.ForeignKey(Instrument, verbose_name="仪器", on_delete=models.DO_NOTHING, null=True)
    #第n步
    step = models.IntegerField(verbose_name='序号', null=True)
    # 用时
    time = models.IntegerField(verbose_name='用时', null=True)