# Read ProduceReport
# Write all contents of this file to a Second Sheet in the current workbook
# Display Grand Total and Average of AMT SOLD and TOTAL

import openpyxl as xl
from openpyxl.styles import Font

wb = xl.Workbook()

#

write_sheet = wb.create_sheet('Second Sheet')

read_wb = xl.load_workbook('ProduceReport.xlsx')
read_ws = read_wb['ProduceReport']

maxC = read_ws.max_column
maxR = read_ws.max_row

