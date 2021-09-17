import tianqi_API
import xlrd
import xlwt


a = []  # 总数据的数据
Excel = xlrd.open_workbook(filename=r'城市.xls')
Table1 = Excel.sheets()[0]
hang = Table1.nrows

for i in range(hang):
    b = Table1.row_values(i)
    a.append(b)

for i in range(1, len(a)):  # 去掉表头内容
    chengshi = a[i][0]
    b = tianqi_API.re(chengshi)
    a[i][2] = b['desc']
    if b['desc'] == a[i][1]:
        a[i][3] = '成功'
    else:
        a[i][3] = '失败'


excel = xlwt.Workbook()  # 只是创建了Excel文件，还未保存
table = excel.add_sheet("子表")  # Excel文件的子表
for i in range(len(a)):
    for j in range(len(a[i])):
        table.write(i, j, a[i][j])  # i，j分别是单元格的坐标，i表示行数，j表示列数
excel.save("城市.xls")
