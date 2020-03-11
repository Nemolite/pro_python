import openpyxl
wb = openpyxl.load_workbook('exfile.xlsx')
sheet = wb['main']

val = sheet['A1'].value
print(val)
val = sheet['B1'].value
print(val)
print(type(val))
wb.close()

wb2 = openpyxl.load_workbook('exfile2.xlsx')
sheet2 = wb['Лист1']
sheet2['B1'] = val
wb.save('exfile2.xlsx')

wb2.close()
