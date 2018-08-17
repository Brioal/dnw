from django.db import models

# Create your models here.


# 折扣表
class Discount(models.Model):
    discount = models.FloatField(verbose_name="折扣")
    def __str__(self):
        return str(self.discount)
    class Meta:
        verbose_name = "折扣录入"
        verbose_name_plural = "折扣录入"



# class Order(models.Model):
