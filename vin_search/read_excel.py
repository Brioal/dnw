import os, django
import  xlrd
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vin码查询.settings")  # project_name 项目名称
django.setup()


from vin_search.models import PRODUCT_CARTYPE
data_in_db = PRODUCT_CARTYPE.objects.all()

book = xlrd.open_workbook("F://已处理数据//车型查询.xlsx")
sh = book.sheet_by_index(0)
query_setlist=[]
for rx in range(1, sh.nrows):
    code = sh.row(rx)[3].value
    info = sh.row(rx)[1].value

    pattern = '\w+'
    text = code
    result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
    product_model_excel = ''
    if len(result_list) == 1:
        if len(result_list[0]) > 4:
            product_model_excel = result_list[0]
    if(product_model_excel != ''):
        result = data_in_db.filter(product_code=product_model_excel, car_info=info)
        if not result.exists():
            insert_flag = 1
            for query_set in query_setlist:
                if (query_set.product_code==product_model_excel and query_set.car_info==info):
                    insert_flag = 0
                    break
            if insert_flag == 1:
                query_setlist.append(PRODUCT_CARTYPE(product_code=product_model_excel, car_info=info))




PRODUCT_CARTYPE.objects.bulk_create(query_setlist)
