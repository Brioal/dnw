from modulefinder import Module

from django.db import models

# Create your models here.


# 总店
from users.models import MyUser


class HeadStore(models.Model):
    type = models.IntegerField(default=0, editable=False)
    name = models.CharField(default="", max_length=100, verbose_name="名称")
    class Meta:
        verbose_name = u'    总店'
        verbose_name_plural = verbose_name
    def __str__(self):
        """重载函数，使自定义字符串能打印"""
        return self.name


# 省代
class ProvinceAgent(models.Model):
    type = models.IntegerField(default=1, editable=False)
    name = models.CharField(default="", max_length=100, verbose_name="名称")
    parent = models.ForeignKey(HeadStore, verbose_name="所属机构", related_name='son', on_delete=models.CASCADE,)
    admin_user = models.ForeignKey(MyUser, verbose_name="管理员", related_name='user_org', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        verbose_name = u'   省代'
        verbose_name_plural = verbose_name
    def __str__(self):
        """重载函数，使自定义字符串能打印"""
        return self.name

# 市代
class CityAgent(models.Model):
    type = models.IntegerField(default=2, editable=False)
    name = models.CharField(default="", max_length=100, verbose_name="名称")
    parent = models.ForeignKey(ProvinceAgent, verbose_name="所属机构", related_name='son', on_delete=models.CASCADE,)
    admin_user = models.ForeignKey(MyUser, verbose_name="管理员", related_name='user_org1', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        verbose_name = u'  市代'
        verbose_name_plural = verbose_name
    def __str__(self):
        """重载函数，使自定义字符串能打印"""
        return self.name
# 门店
class LastStore(models.Model):
    type = models.IntegerField(default=3, editable=False)
    name = models.CharField(default="", max_length=100, verbose_name="名称")
    parent = models.ForeignKey(CityAgent, verbose_name="所属机构", related_name='son', on_delete=models.CASCADE,)
    admin_user = models.ForeignKey(MyUser, verbose_name="管理员", related_name='user_org2', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        verbose_name = u' 门店'
        verbose_name_plural = verbose_name
    def __str__(self):
        """重载函数，使自定义字符串能打印"""
        return self.name
