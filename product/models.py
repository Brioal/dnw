from django.db import models
#产品
class Product(models.Model):
    #产品名
    name = models.CharField(max_length=30, verbose_name="产品名", null=True)
    #价格
    price = models.CharField(max_length=30, verbose_name="价格", null=True)
    #数量
    number = models.IntegerField(verbose_name = '数量')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "产品录入"
        verbose_name_plural = "产品录入"
#器械
class Instrument(models.Model):
    #器械名称
    name = models.CharField(max_length=30, verbose_name="器械名", null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "器械录入"
        verbose_name_plural = "器械录入"
