from django.shortcuts import render

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_exempt

from vin_search.models import VIN_PRODUCT, PRODUCT_CARTYPE

from .check_vin import check_vin


code_year_dict = {'1': 2001, '9': 2009, 'S': 2025, '2': 2002, '7': 2007, 'L': 2020, '8': 2008, 'F': 2015, 'J': 2018, 'H': 2017, 'K': 2019, '4': 2004, 'D': 2013, '6': 2006, 'C': 2012, 'G': 2016, 'V': 2027, 'T': 2026, 'R': 2024, 'A': 2010, 'X': 2029, 'B': 2011, 'E': 2014, 'N': 2022, 'Y': 2030, 'P': 2023, '5': 2005, '3': 2003, 'W': 2028, 'M': 2021}
code = '1'

def getProductByVin(vin):
    vin = vin.upper()
    global code
    code = vin[9]
    vin = vin[:8]
    # 获取年份码
    product_list = []
    query_result = VIN_PRODUCT.objects.filter(vin_code=vin)
    for result in query_result:
        product_list.append(result.product_code)
    return product_list
def getCarTypeByProduct(product_list):
    carInfo_list = []
    query_result_list = []
    # 根据年份码获取车型年份
    year = code_year_dict[code]
    for product in product_list:
        query_result_list.append(PRODUCT_CARTYPE.objects.filter(product_code=product))
    for query_result in query_result_list:
        for result in query_result:
            if((result.car_info).find(str(year)) != -1):
                carInfo_list.append(result.car_info)
    carInfo_list = (list(set(carInfo_list)))
    carInfo_list.sort()
    carInfo_table_list = []
    carInfo_table = []
    count = 0
    for carInfo in carInfo_list:
        if(count == 3):
            count = 0
        if(count == 0):
            carInfo_table = []
            carInfo_table_list.append(carInfo_table)
        carInfo_table.append(carInfo)
        count = count + 1
    return carInfo_table_list

@xframe_options_exempt
def carTypeView(request):
    if(request.method == "GET"):
        try:
            vin = request.GET['vin']
        except:
            return render(request, 'vin_search/vin_check_false.html')
        if(check_vin(vin) == False):
            return render(request, 'vin_search/vin_check_false.html')
        vin = str(vin)
        product_list = getProductByVin(vin=vin)
        carInfo_table_list = getCarTypeByProduct(product_list=product_list)
        context = {
            'vin': vin,
            'carInfo_table_list': carInfo_table_list,
        }

        return render(request, 'vin_search/vin_cartype_display.html', context)


def test(request):
    context = {

    }
    return render(request, 'vin_search/test.html', context)