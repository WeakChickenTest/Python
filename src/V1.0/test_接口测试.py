import requests
import xlrd
import xlwt

Excel = xlrd.open_workbook(filename=r'../测试表格.xlsx')
table = Excel.sheets()[0]
a1 = table.nrows# 获取有多少列table.col_values(0)
biaotou0 = []
biaotou1 = a2 = table.row_values(0)
biaotou1.extend(["实际结果","是否通过"])# 将获取到的表头添加2个字段:实际结果和是否通过
print(biaotou1)
# 创建一个新的表以及子表
newExcel = xlwt.Workbook()
newTable = newExcel.add_sheet("子表")

# 把新表头写到子表中
for key in range (len(biaotou1)):
    newTable.write(0, key, biaotou1[key])


url = "http://wthrcdn.etouch.cn/weather_mini"# 接口地址
for i in range(1,a1):# 有多少列数据，就循环多少次
    a2 = table.row_values(i)# 获取每一行的元素
    b1 = a2[0]
    canshu = {"city":b1}
    re = requests.get(url=url,params=canshu)
    html = re.json()
    a2.append(html["desc"])
    print(html)
    while "" in a2:
        a2.remove("")

    if html["desc"]==a2[1]:
        a2.append("测试通过")
    else:
        a2.append("测试未通过")
    print(a2)
