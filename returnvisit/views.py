from django.shortcuts import render
import datetime
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import back_plan
from store.models import Customer
#返回提示时所需json数据
def get_back(request):
    #角色
    role = request.user.job
    today = datetime.datetime.now()
    back_customer = back_plan.objects.filter(back_data__year=str(today.year),
                                             back_data__month=str(today.month),
                                             back_data__day=str(today.day),
                                             )#state=0,back_state=False
    back_customer = back_customer.values()
    back_customer = [entry for entry in back_customer]
    print(back_customer)
    dict={}
    dict["success"] = ''
    dict["message"] = ''
    dict['role'] = ''
    dict['number']=''
    if(len(back_customer)==0):
        dict["success"] = 'false'
        dict["message"] = '今日无回访客户'
    else:
        dict["success"] = 'true'
        dict['role'] = str(role)
        dict['number'] = str(len(back_customer))
    return HttpResponse(json.dumps(dict))
#返回回访列表所需的json数据
def get_back_list(request):
    today = datetime.datetime.now()
    back_customer = back_plan.objects.filter(back_data__year=str(today.year),
                                            back_data__month=str(today.month),
                                            back_data__day=str(today.day),)
    back_customer = back_customer.values()
    back_customer = [entry for entry in back_customer]
    dict = {}
    dict["success"]=''
    dict["message"]=''
    dict["data"] = []
    if(len(back_customer)==0):
        dict["success"]='false'
        dict["message"]="今日没有需回访的客户"
    else:
        dict["success"] = 'true'
        for b_customer in back_customer:
            #获取回访计划所对应的客户
            customer = Customer.objects.filter(id=b_customer['back_customer_id'])
            customer = customer.values()
            customer = [entry for entry in customer]
            temp_c = customer[0]
            list_inf = {}
            list_inf['id'] = b_customer['id']
            list_inf['name'] = temp_c['name']
            list_inf['phone'] = temp_c['phone']
            list_inf['back_state'] = b_customer['back_state']
            dict["data"].append(list_inf)
    print(dict)
    return HttpResponse(json.dumps(dict))
#跳转回访列表视图
def back_list(request):
    return render(request, 'returnvisit/now_back_customerlist.html')