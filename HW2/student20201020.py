#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

num = ws.max_row - 1
a = int(num * 0.3 // 2)
b = int((num * 0.7 - a) // 2)
c = (num - (a + b) * 2) // 2 
A1 = list(0 for i in range(a))
A2 = list(0 for i in range(a))
B1 = list(0 for i in range(b))
B2 = list(0 for i in range(b))
C1 = list(0 for i in range(c))
C2 = list(0 for i in range(c))

row_id = 1
for row in ws:
	if row_id != 1:
		total = ws.cell(row = row_id, column = 7).value
		if total > A1[0]:
			A1[0] = total
			A1.sort()
			ws.cell(row = row_id, column = 8).value = 'A+'
			continue
		elif total > A2[0]:
			A2[0] = total
			A2.sort()
			ws.cell(row = row_id, column = 8).value = 'A0'
			continue
		elif total > B1[0]:
			B1[0] = total
			B1.sort()
			ws.cell(row = row_id, column = 8).value = 'B+'
			continue		
		elif total > B2[0]:
			B2[0] = total
			B2.sort()
			ws.cell(row = row_id, column = 8).value = 'B0'
			continue	
		elif total > C1[0]:
			C1[0] = total
			C1.sort()
			ws.cell(row = row_id, column = 8).value = 'C+'
			continue	
		elif total > C2[0]:
			C2[0] = total
			C2.sort()
			ws.cell(row = row_id, column = 8).value = 'C0'
			continue
	row_id += 1

wb.save("student.xlsx")
	
