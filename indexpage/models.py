from django.db import models

# Create your models here.

class Notice(models.Model):
    message = models.CharField(max_length=1000, verbose_name="消息内容")
    class Meta:
        verbose_name = u'  通知消息'
        verbose_name_plural = verbose_name
    def __str__(self):
        """重载函数，使自定义字符串能打印"""
        return self.message