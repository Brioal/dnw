import os, django
import xlrd
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vin码查询.settings")  # project_name 项目名称
django.setup()

from vin_search.models import VIN_PRODUCT
data = VIN_PRODUCT.objects.all()

file_list = os.listdir("F://已处理数据//excel1")
vin_product_list = []
for file in file_list:
    path = r"F://已处理数据//excel1//" + file
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_index(0)
    query_setlist = []
    n = 0
    for rx in range(1, sh.nrows):
        code = sh.row(rx)[1].value
        info = sh.row(rx)[26].value
        text = str(code)
        pattern = '\w+'
        result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
        product = ''
        for result in result_list:
            if len(result) > len(product):
                product = result
        pattern = '\w+'
        text = str(info)
        result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
        recognition_code_list = []
        for result in result_list:
            if len(result) == 8:
                recognition_code_list.append(result)
        recognition_code_set = set(recognition_code_list)
        for vin in recognition_code_set:
            result = data.filter(vin_code=vin, product_code=product)
            if not result.exists():
                insert_flag = 1
                for query_set in query_setlist:
                    if (query_set.vin_code == vin and query_set.product_code == product):
                        insert_flag = 0
                        break
                if insert_flag == 1:
                    vin_product_list.append(VIN_PRODUCT(vin_code=vin, product_code=product))


VIN_PRODUCT.objects.bulk_create(vin_product_list)
