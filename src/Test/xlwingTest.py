import xlwings


# 初始设置
excel = xlwings.App(visible=True, add_book=False)
excel.display_alerts = False
excel.screen_updating = False

"""
# 打开Excel文件
wb = excel.books.open(filePath)
# 保存Excel文件
wb.save()
# 关闭Excel文件
wb.close()
# 结束程序
excel.quit()
"""

# 新建Excel文件，保存为testExcel.xlsx，保存在E:/Python/src目录下
wb1 = excel.books.add()
wb1.save(r'E:/Python/src/杂七杂八/testExcel.xlsx')
wb1.close()
print('Excel表格创建成功！')

# 新建Excel文件，在sheet1的A1和A2单元格中填充数据
wb2 = excel.books.add()
wb2.sheets['Sheet1'].range('A1').value = '人生苦短'
wb2.sheets['Sheet1'].range('A2').value = '我用Python'
wb2.save(r'e:/Python/src/杂七杂八/testExcel1.xlsx')
wb2.close()
print('Sheet1的单元格填充成功！')

# 填充testExcel1.xlsx文件sheet1中的A3单元格
wb3 = excel.books.open(r"e:/Python/src/杂七杂八/testExcel1.xlsx")
wb3.sheets['Sheet1'].range('A3').value = '你用什么?'
wb3.save()
wb3.close()
excel.quit()
