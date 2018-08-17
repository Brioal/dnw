from django.db import models

# Create your models here.
class VIN_PRODUCT(models.Model):
    vin_code = models.CharField(max_length=8, verbose_name="vin码")
    product_code = models.CharField(max_length=32)

    def __str__(self):
        return self.vin_code + "," + self.product_code
    class Meta:
        verbose_name = "VIN产品"
        verbose_name_plural = "VIN产品列表"


class PRODUCT_CARTYPE(models.Model):
    product_code = models.CharField(max_length=128)
    car_info = models.CharField(max_length=128)
