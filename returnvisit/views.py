from django.shortcuts import render
import datetime
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import back_plan
from store.models import Customer
#返回提示时所需json数据 done
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

#返回回访列表所需的json数据 done
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


#跳转回访列表视图 done
def back_list(request):
    return render(request, 'returnvisit/now_back_customerlist.html')


#按确定按钮改回访状态接口
@csrf_exempt
def set_back_state(request):
    id = request.GET.get('id')
    modify_comster_state = back_plan.objects.get(id=id)
    modify_comster_state.back_state = True
    modify_comster_state.save(update_fields=["back_state"])
    dict  = {}
    dict["success"] = True
    return HttpResponse(json.dumps(dict))


#添加回访计划所需视图

#搜索显示将要回访的人回访计划 done
@csrf_exempt
def display_serach_back(request):
    #客服id
    service_id = request.user.id
    print(service_id)
    keyword = request.POST.get('key')
    back_customer = Customer.objects.filter(web_staff=service_id, name__contains=keyword)
    print(back_customer)
    back_customer = back_customer.values()
    back_customer = [entry for entry in back_customer]
    dict = {}
    dict["success"] = ''
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    if (len(back_customer) == 0):
        dict["success"] = 'false'
        dict["message"] = "未搜索到任何客户"
    else:
        dict["success"] = 'true'
        dict["total"] = len(back_customer)
        for b_customert in back_customer:
            list_inf = {}
            list_inf['id'] = b_customert['id']
            list_inf['name'] = b_customert['name']
            list_inf['state'] = b_customert['state']
            dict["data"].append(list_inf)
    return HttpResponse(json.dumps(dict))
#存储回访计划 done
@csrf_exempt
def save_back_plan(request):
    #获取客户id
    customer_id = request.POST.get('id')
    #获取客服的电话号
    s_phon = request.user.phone_number
    s_customer = back_plan(back_data=datetime.date.today(), back_state=False, back_customer=customer_id, service_phon=s_phon)
    s_customer.save()
    dict = {}
    dict["success"] = False
    dict["message"] = '新建回访计划失败'
    dict["data"] = []
    if(s_customer.id>0):
        dict["success"] = False
        dict["message"] = ''
    return HttpResponse(json.dumps(dict))
#还需写添加回访计划的删除和修改




#添加回访计划列表视图 done
@csrf_exempt
def get_add_back_list(request):
    today = datetime.datetime.now()
    #获得客服电话号
    s_phon = request.user.phone_number
    back_customer = back_plan.objects.filter(back_data__year=str(today.year),
                                             back_data__month=str(today.month),
                                             back_data__day=str(today.day),
                                             service_phon=s_phon)
    back_customer = back_customer.values()
    back_customer = [entry for entry in back_customer]
    dict = {}
    dict["success"] = ''
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    if (len(back_customer) == 0):
        dict["success"] = 'false'
        dict["message"] = "今日还未添加任何回访计划"
    else:
        dict["success"] = 'true'
        dict["total"] = len(back_customer)
        for b_customer in back_customer:
            #获取添加回访计划所对应的客户
            customer = Customer.objects.filter(id=b_customer['back_customer_id'])
            customer = customer.values()
            customer = [entry for entry in customer]
            temp_c = customer[0]
            list_inf = {}
            list_inf['id'] = b_customer['id']
            list_inf['name'] = temp_c['name']
            list_inf['back_data'] = b_customer['back_data']
            list_inf['back_state'] = b_customer['back_state']
            list_inf['shop_state'] = temp_c['state']
            dict["data"].append(list_inf)
    return HttpResponse(json.dumps(dict, default=str))
#****************************************************************
#历史回访记录

#默认获得的历史回访记录列表 done
def history_record(request):
    # s_date = request.GET.get('s_date')
    # e_date = request.GET.get('e_date')
    # 获得客服电话号
    s_phon = request.user.phone_number
    e_date = datetime.datetime.now()
    e_date = datetime.date(e_date.year, e_date.month, e_date.day)
    s_date = datetime.date(2016, 8, 8)
    history_customer = back_plan.objects.filter(back_data__range=(s_date, e_date), service_phon=s_phon)
    history_customer = history_customer.values()
    history_customer = [entry for entry in history_customer]
    dict = {}
    dict["success"] = ''
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    if(len(history_customer)==0):
        dict["success"] = 'false'
        dict["message"] = "暂无历史回访记录"
    else:
        dict["success"] = 'true'
        dict["total"] = len(history_customer)
        for h_customer in history_customer:
            customer = Customer.objects.filter(id=h_customer['back_customer_id'])
            customer = customer.values()
            customer = [entry for entry in customer]
            temp_c = customer[0]
            list_inf = {}
            list_inf['id'] = h_customer['id']
            list_inf['name'] = temp_c['name']
            list_inf['back_data'] = h_customer['back_data']
            list_inf['back_state'] = h_customer['back_state']
            list_inf['shop_state'] = temp_c['state']
            dict["data"].append(list_inf)
    return HttpResponse(json.dumps(dict, default=str))
#获取搜索结果
@csrf_exempt
def get_history_search_back(request):
    #获得开始时间
    s_date = request.POST.get('s_date')
    s_list = s_date.split('-', 2)
    s_date = datetime.date(int(s_list[0]), int(s_list[1]), int(s_list[2]))
    #获得结束时间
    e_date = request.POST.get('e_date')
    e_list = e_date.split('-', 2)
    e_date = datetime.date(int(e_list[0]), int(e_list[1]), int(e_list[2]))
    #获得客户姓名关键字
    keyword = request.POST.get('key')
    dict = {}
    dict["success"] = ''
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    #存储客户的id
    list = []
    #获得客户对象
    c_id = request.user.id
    customer = Customer.objects.filter(web_staff=c_id, name__contains=keyword)
    customer = customer.values()
    customer = [entry for entry in customer]
    for cs in customer:
        list.append(cs['id'])
    # 获得客服电话号
    s_phon = request.user.phone_number
    back_customer = back_plan.objects.filter(back_data__range=(s_date, e_date), service_phon=s_phon)
    back_customer = back_customer.values()
    back_customer = [entry for entry in back_customer]
    if(len(back_customer)):
        dict["success"] = False
        dict["message"] = '无任何历史回访记录'
    else:
        dict["success"] = True
        dict["total"] = len(back_customer)
        for b_customer in back_customer:
            list_inf={}
            b_id = -1
            for index in rang(len(list)):
                if(list[index]==b_customer['back_customer_id']):
                    b_id = list[index]
                    break
            t_customer = Customer.objects.filter(id = b_id)
            t_customer = t_customer.values()
            t_customer = [entry for entry in t_customer]
            temp_c = t_customer[0]
            list_inf['name'] = temp_c['name']
            list_inf['state'] = b_customer['back_state']
            list_inf['date'] = b_customer['back_data']
            list_inf['shop_state'] = temp_c['state']
            dict["data"].append(list_inf)
    return HttpResponse(json.dumps(dict, default=str))
#*********************************************************************
#顾客状态查询
@csrf_exempt
def get_customer_state_list(request):
    keyword = request.POST.get('key')
    # 获得客服电话号
    service_id = request.user.id
    customer = Customer.objects.filter(web_staff=service_id, name__contains=keyword)
    customer = customer.values()
    customer = [entry for entry in customer]
    dict = {}
    dict["success"] = ''
    dict["message"] = ''
    dict["total"] = 0
    dict["data"] = []
    if(len(customer)==0):
        dict["success"]=False
        dict["message"] = '未获得任何客户状态'
    else:
        dict["success"] = True
        dict["total"] = len(customer)
        for cs in customer:
            list_inf={}
            list_inf['name'] = cs['name']
            list_inf['phone'] = cs['phone']
            list_inf['state'] = cs['state']
            dict["data"].append(list_inf)
    return HttpResponse(json.dumps(dict))
