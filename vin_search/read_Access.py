import pypyodbc
import re
import os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vin码查询.settings")  # project_name 项目名称
django.setup()

from vin_search.models import VIN_PRODUCT
data = VIN_PRODUCT.objects.all()

connection = pypyodbc.win_connect_mdb('F://已处理数据//280//test.mdb')

with open('F://已处理数据//280//test.txt', 'r') as f:
    vin_product_list = []
    for word in f.readlines():
        word = word.replace('\n', '')
        word = "[" + word + "]"
        SQL = "select 产品型号, 识别代号 from " + word  # 识别代号中需要去掉\n
        cursor = connection.cursor()
        cursor.execute(SQL)
        cursor = cursor.fetchall()
        total_num = len(cursor)
        now_num = 0
        process_percent = now_num / total_num
        old_percent = 0
        for row in cursor:
            now_num = now_num + 1
            process_percent = now_num / total_num
            if(process_percent - old_percent) > 0.001:
                old_percent = process_percent
                print_percent = round(process_percent, 4)
                print("当前数据库", word,", 处理进度为：", print_percent)
            # 正则表达：产品型号
            pattern = '\w+'
            text = str(row[0])
            result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
            product = ''
            for result in result_list:
                if len(result) > len(product):
                    product = result
            # 正则表达：识别代码
            pattern = '\w+'
            text = str(row[1])
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
                    for query_set in vin_product_list:
                        if (query_set.vin_code == vin and query_set.product_code == product):
                            insert_flag = 0
                            break
                    if insert_flag == 1:
                        vin_product_list.append(VIN_PRODUCT(vin_code=vin, product_code=product))

    VIN_PRODUCT.objects.bulk_create(vin_product_list)
