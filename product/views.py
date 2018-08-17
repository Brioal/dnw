
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Product
from django.views.decorators.csrf import csrf_exempt
#ajax获取列表信息
@csrf_exempt
def get_product_json(request):
    #处理接收的json格式
    pagSize = request.POST.get('pageSize')
    pagSize = int(pagSize)
    pageIndex = request.POST.get('pageIndex')
    pageIndex = int(pageIndex)
    name = request.POST.get('productName')
    start = pageIndex*pagSize-pagSize
    #print(start)
    end = pageIndex*pagSize
    dict = {}
    product_List = Product.objects.all()
    product_List = product_List.values()
    product_List = [entry for entry in product_List]
    number_list = len(product_List)
    if(name==''):
       #传到后台的json
       product_List = Product.objects.all()
       product_List = product_List.values()
       product_List = [entry for entry in product_List]
       product_List = product_List[start:end]
       dict['total'] = number_list
       dict['rows'] = []
       for p_list in product_List:
          dict['rows'].append(p_list)
    else:
        product_List =Product.objects.filter(name__contains=name)
        product_List = product_List.values()
        product_List = [entry for entry in product_List]
        product_List = product_List[start:end]
        dict['total'] = number_list
        dict['rows'] = []
        for p_list in product_List:
            dict['rows'].append(p_list)


    return HttpResponse(json.dumps(dict))

#ajax搜索框自动提示
@csrf_exempt
def search_auto_result(request):
    keyword = request.GET.get('kwd')
    # print(keyword)
    product_List = Product.objects.filter(name__contains=keyword)
    product_List = product_List.values()
    product_List = [entry for entry in product_List]
    dict = {}
    dict['name'] = []
    for atuo_list in product_List:
           dict['name'].append(atuo_list['name'])
    return HttpResponse(json.dumps(dict))

#测试一
def testone(request):
    return render(request, "product/test.html")