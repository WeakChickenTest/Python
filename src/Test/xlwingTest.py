import xlwings


# 初始设置
excel = xlwings.App(visible=True, add_book=False)
excel.display_alerts = False
excel.screen_updating = False
"""
# Excel文件
filePath = r'../测试表格.xls'

# 打开Excel文件
wb1 = excel.books.open(filePath)
# 保存Excel文件
wb1.save()
# 关闭Excel文件
wb1.close()
# 结束程序
excel.quit()

# 新建Excel文件，保存为testExcel.xlsx，保存在E:/Python/src目录下
wb2 = excel.books.add()

wb2.save(r'E:/Python/src/testExcel.xlsx')
wb2.close()
excel.quit()
print('Excel表格创建成功！')

"""
# 新建Excel件，在sheet1的A1单元格中填充数据
wb3 = excel.books.add()
wb3.sheets['Sheet1'].range('A1').value = '人生苦短'
wb3.sheets['Sheet1'].range('A2').value = '我用Python'


wb3.save(r'e:/Python/src/testExcel1.xlsx')
wb3.close()
print('Sheet1的单元格填充成功！')


wb = excel.books.open(r"e:/Python/src/testExcel1.xlsx")
wb.sheets['Sheet1'].range('A3').value = '你用什么?'

wb.save()
wb.close()
excel.quit()


