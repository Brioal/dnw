from django.shortcuts import render
from .models import WareHouse, Supplier
from django.shortcuts import render
import datetime
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# 仓库管里视图***************************************************************
#跳转到仓库管理页面 done
def enter_wmanagement(request):
    return render(request, 'Inventory_app/warehouse_management.html')
    # return render(request, 'Inventory_app/base.html')
#添加仓库 done
@csrf_exempt
def add_new_warehouse(request):
    #仓库名称
    content = request.POST.get('name')
    #仓库状态
    state = str(request.POST.get('state'))
    print(state)
    #建仓时间
    new_warehouse = WareHouse(wName=content, wState=state, build_WareHouse_time=datetime.date.today())
    new_warehouse.save()
    dict={}
    dict['success'] = False
    dict["message"] = '创建仓库失败'
    if(new_warehouse.id>0):
        dict['success']=True
        dict["message"] = ''
    return HttpResponse(json.dumps(dict))
#返回仓库列表 done
@csrf_exempt
def get_warehouse_list(request):
    #获得所有的已添加仓库
    all_warehouse = WareHouse.objects.all()
    all_warehouse = all_warehouse.values()
    all_warehouse = [entry for entry in all_warehouse]
    dict={}
    dict["success"] = False
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    if(len(all_warehouse)==0):
        dict["success"] = False
        dict["message"] = '无任何已建仓库'
    else:
        dict["success"] = True
        dict["total"] = len(all_warehouse)
        for a_warehouse in all_warehouse:
            list_warehouse = {}
            list_warehouse["id"] = a_warehouse["id"]
            list_warehouse["name"] = a_warehouse["wName"]
            list_warehouse["state"] = a_warehouse["wState"]
            list_warehouse["build_WareHouse_time"] = a_warehouse["build_WareHouse_time"]
            dict["data"].append(list_warehouse)
    return HttpResponse(json.dumps(dict,default=str))
#*********************************************************************************************
#供应商管理
#添加供应商
@csrf_exempt
def add_supplier(request):
    #供应商
    s_name = request.POST.get('s_name')
    #单位电话
    u_phone = request.POST.get('u_phone')
    #联系人
    c_name = request.POST.get('c_name')
    #联系人电话
    c_phone = request.POST.get('c_phone')
    supplier = Supplier(sName=s_name, companyPhone=u_phone, contactPeople=c_name, contactPhone=c_phone)
    supplier.save()
    dict = {}
    dict["success"] = False
    dict["message"] = '添加供应商失败'
    if(supplier.id>0):
        dict["success"] = False
        dict["message"] = '添加供应商失败'
    return HttpResponse(json.dumps(dict))




