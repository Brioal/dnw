from django.db import models

#仓库表
class WareHouse(models.Model):
    #仓库名称
    wName = models.CharField(max_length=30, verbose_name="仓库名称", null=True)
    #状态
    wState = models.CharField(max_length=30, verbose_name="仓库状态", null=True)
    #建仓库时间
    build_WareHouse_time = models.DateField(null=True, blank=True)
#供应商
class Supplier(models.Model):
    #供应商名称
    sName = models.CharField(max_length=30, verbose_name="供应商名称", null=True)
    #单位电话
    companyPhone = models.CharField(max_length=30,  null=True)
    #联系人
    contactPeople = models.CharField(max_length=30,  null=True)
    #联系人电话
    contactPhone = models.CharField(max_length=30,  null=True)
#进货单
class PurchaseOrder(models.Model):
    #商品名称
    pName = models.CharField(max_length=30, verbose_name="商品名称", null=True)
    #商品数量
    pNumber = models.IntegerField(null=True, blank=True)
    #单价
    unitPrice = models.IntegerField(null=True, blank=True)
    #单位
    unit = models.CharField(max_length=30, verbose_name="单位", null=True)
    #类型
    pType = models.CharField(max_length=30, verbose_name="类型", null=True)
    #供应商
    supplier = models.ForeignKey(Supplier, verbose_name="所属供应商", related_name='sname', on_delete=models.DO_NOTHING, null=True, blank=True)
    #仓库
    wHouse = models.ForeignKey(WareHouse, verbose_name="所属仓库", related_name='wname', on_delete=models.DO_NOTHING, null=True, blank=True)
    #经手人姓名
    handManName = models.CharField(max_length=30,  null=True)
    #经手人电话
    handManPhone = models.CharField(max_length=30, null=True)
    #进货日期
    orderDate = models.DateTimeField()
    #备注
    remarks = models.TextField(null=True, blank=True)
    #总金额
    totalPrice = models.IntegerField(null=True, blank=True)
#库之间的调拨记录
class Record_transfer_library(models.Model):
    #商品名称
    pName = models.CharField(max_length=30,  null=True)
    #数量
    pNumber = models.IntegerField(null=True, blank=True)
    #单价
    unitPrice = models.IntegerField(null=True, blank=True)
    #单位
    unit = models.CharField(max_length=30,  null=True)
    #总金额
    totalPrice = models.IntegerField(null=True, blank=True)
    #类型
    type = models.CharField(max_length=30,  null=True)
    #出仓库
    out_w = models.ForeignKey(WareHouse,  related_name='outwname', on_delete=models.DO_NOTHING, null=True, blank=True)
    #进仓库
    in_w = models.ForeignKey(WareHouse,  related_name='inwname', on_delete=models.DO_NOTHING, null=True, blank=True)
    # 经手人姓名
    handManName = models.CharField(max_length=30, null=True)
    # 经手人电话
    handManPhone = models.CharField(max_length=30, null=True)
    #调拨时间
    trasfer_date = models.DateTimeField()