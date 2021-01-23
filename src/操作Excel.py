import xlwt# 写Excel表格
import xlrd# 读Excel表格

excel = xlwt.Workbook()# 只是创建了Excel文件，还未保存
table = excel.add_sheet("子表")# Excel文件的子表
a = [["参数1","预期结果"],#,"实际结果","是否通过"
    ["北京","OK"],
    ["上海","OK"],
    ["Python","invilad-citykey"],
    ["深圳","OK"],
    ["杭州","OK"]]
for i in range(len(a)):
    for j in range(len(a[i])):
        table.write(i,j,a[i][j])# i，j分别是单元格的坐标，i表示行数，j表示列数
excel.save("测试表格.xlsx")

Excel = xlrd.open_workbook(filename=r'测试表格.xlsx')# Excel表格的路径，Windows环境下，如果文件不在当前目录下，需要在路径前加上小写的r
table = Excel.sheets()[0]# 第一种选择子表的方法，数字0表示选择第一张子表
# table = Excel.sheet_by_index(0)# 第二种选择子表的方法，数字0表示选择第一张子表
# table = Excel.sheet_by_name('子表')# 第三种选择子表的方法，直接写子表名，写不存在的子表名会报错

a1 = table.row_values(0)# 获取整行数据，必须指定获取的行号
print(a1)
a2 = table.col_values(0)# 获取整列的数据，必须指定获取的列号
print(a2)
a3 = table.row(1)[0].value# 先获取某一行，返回列表，再通过下标获取具体的元素，1表示第2行，0表示第1列
print(a3)
a4 = table.col(1)[0].value# 先获取某一列，返回列表，再通过下标获取具体的元素，1表示第2列，0表示第1行
print(a4)
a5 = table.cell(0,1).value# 直接通过表格的坐标获取内容
print(a5)
a6 = table.nrows# 获取有多少行
print(a6)
a7 = table.ncols# 获取有多少列
print(a7)
a8 = Excel.sheet_names()# 获取所有子表名，返回列表
print(a8)
print(f"这个Excel表总共有{len(a8)}个子表,第一张子表有{a6}行{a7}列")