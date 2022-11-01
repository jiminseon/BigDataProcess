#!/usr/bin/python3
import sys
import calendar

input = sys.argv[1]
output = sys.argv[2]

with open(output, "wt") as wp:
	with open(input, "rt") as rp:
		twoList = []
		dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
		for line in rp:
			str_arr = line.strip()
			str_arr = str_arr.split(",")
			date = str_arr[1].split("/")
			str_arr[1] = dayofweek[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))]
			line = []
			for i in range(len(str_arr)):
				line.append(str_arr[i])
			twoList.append(line)

		for i in range(len(twoList)):
			wp.write(twoList[i][0] + "," + twoList[i][1] + " " + twoList[i][2] + "," + twoList[i][3] + "\n")
