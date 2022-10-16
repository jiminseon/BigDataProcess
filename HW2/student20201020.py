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
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		total = ws.cell(row = row_id, column = 7).value
		print(total)
		if total > A1[0]:
			A1[0] = total
			A1.sort()
			ws.cell(row = row_id, column = 8).value = 'A+'
			row_id += 1
			continue
		elif total > A2[0]:
			A2[0] = total
			A2.sort()
			ws.cell(row = row_id, column = 8).value = 'A0'
			row_id += 1
			continue
		elif total > B1[0]:
			B1[0] = total
			B1.sort()
			ws.cell(row = row_id, column = 8).value = 'B+'
			row_id += 1
			continue		
		elif total > B2[0]:
			B2[0] = total
			B2.sort()
			ws.cell(row = row_id, column = 8).value = 'B0'
			row_id += 1
			continue	
		elif total > C1[0]:
			C1[0] = total
			C1.sort()
			ws.cell(row = row_id, column = 8).value = 'C+'
			row_id += 1
			continue	
		elif total > C2[0]:
			C2[0] = total
			C2.sort()
			ws.cell(row = row_id, column = 8).value = 'C0'
			row_id += 1
			continue
	row_id += 1

wb.save("student.xlsx")
	
