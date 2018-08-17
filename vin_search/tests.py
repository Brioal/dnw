# Create your tests here.
# import re
# pattern = '\w+'
# text = '日产(NISSAN)牌ZN5040XXYB1Z4型厢式'
# print(re.findall(pattern, text, re.A))  # 返回['ab', 'ab']






# import pypyodbc
# connection = pypyodbc.win_connect_mdb('F:\\test.mdb')
# SQL = "select 产品型号, 识别代号 from 271"
# cursor = connection.cursor()
# cursor.execute(SQL)
# for row in cursor:
#     print(row)

#
# import xlrd
# book = xlrd.open_workbook("F://车型查询.xlsx")
# sh = book.sheet_by_index(0)
# for rx in range(sh.nrows):
#     print(sh.row(rx))
#


#
# # 正则表达：识别代码
# import re
# pattern = '\w+'
# text = r'LNVU1CA3×××××××××LNVU1CA4×××××××××LA92DFE8×××LPC×××'
# result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
# recognition_code_list = []
# for result in result_list:
#     if len(result) == 8:
#         recognition_code_list.append(result)
# print(recognition_code_list)

# # 正则表达：产品型号
# import re
# pattern = '\w+'
# text = r'柯斯达(COASTER)牌SCT6705GRB53LEXB型客车'
# result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
# product_model = ''
# for result in result_list:
#     if len(result) > len(product_model):
#         product_model = result
# print(product_model)
#
# # 正则表达：忽略（提车架用）
# import re
# pattern = '\w+'
# text = r'克莱斯勒BJ7270C'
# result_list = re.findall(pattern, text, re.A)  # 返回['ab', 'ab']
# product_model_excel = ''
# if len(result_list) == 1:
#     if len(result_list[0]) > 4:
#         product_model_excel = result_list[0]
# print(product_model_excel)

#
# # 正则表达：车系
# import re
# pattern = '\w+'
# text = r'安驰 威豹 2.8T 手动 柴油版 2009款'
# result_list = text.split(" ")  # 返回['ab', 'ab']
# car_type_list = []
# if len(result_list) == 6:
#     car_type_list = result_list
# print(car_type_list)

# import os
# print(os.listdir("F:\excel1"))