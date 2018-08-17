import  xlrd


#def read_excel_year():
book = xlrd.open_workbook("vin码校验表.xlsx")
sh = book.sheet_by_index(0)
code_year_dict = dict()
for rx in range(0, sh.nrows):
    key = str(sh.row(rx)[0].value)
    value = int(sh.row(rx)[1].value)
    code_year_dict[key] = value
print(code_year_dict)