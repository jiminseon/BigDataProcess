#!/usr/bin/python3
import sys
import calendar

input = sys.argv[1]
output = sys.argv[2]

with open(output, "wt") as wp:
	with open(input, "rt") as rp:
		a = dict()
		dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
		for line in rp:
			str_arr = line.strip()
			str_arr = str_arr.split(",")
			date = str_arr[1].split("/")
			str_arr[1] = dayofweek[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))]
		

			if (str_arr[0] not in a):
				b = {str_arr[1] : str_arr[2], str_arr[1] + "t" : str_arr[3]}
				a[str_arr[0]] = a.get(str_arr[0], b)
			else:
				if (str_arr[1] not in a[str_arr[0]]):
					a[str_arr[0]][str_arr[1]] = str_arr[2] 
					a[str_arr[0]][str_arr[1] + "t"] = str_arr[3]
				else:
					total = int(a[str_arr[0]][str_arr[1]]) + int(str_arr[2])
					a[str_arr[0]][str_arr[1]] = str(total)
					total = int(a[str_arr[0]][str_arr[1] + "t"]) + int(str_arr[3])
					a[str_arr[0]][str_arr[1] + "t"] = str(total)

		keylist = a.keys()	
		for i in keylist:
			for j in dayofweek:
				vehicles = a[i][j]
				trips = a[i][j + "t"]
				wp.write(i + "," + j + " " +  vehicles + "," + trips + "\n")


