#!/usr/bin/python3
import sys

input = sys.argv[1]
output = sys.argv[2]

with open(output, "wt") as wp:
	with open(input, "rt") as rp:
		count = dict()
		for line in rp:
			str_arr = line.strip()
			str_arr = str_arr.split("::")
			genre = str_arr[2].split("|")
			
			for i in range(len(genre)):
				count[genre[i]] = count.get(genre[i], 0) + 1

		keylist = count.keys()
		for key in keylist:
			wp.write(key + " " +  str(count[key]) + "\n")

