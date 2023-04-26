import openpyxl1 as xl

wb = xl.load_workbook('example.xlsx')

sn = wb.sheetnames

print(sn)

sheet1 = wb['Sheet1']
cellA1 = sheet1['A1']

print(sheet1)
print(cellA1)

print(cellA1.value)
print(type(cellA1.value))

print(cellA1.row)
print(cellA1.column)
print(cellA1.coordinate)