from array import *
import csv

T = []
L = []
word = []
with open('trial-1-sentence.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	rows = list(readCSV)
	row_count = len(rows)

	for i in range(0, row_count):
		numrows = len(T)
		print (rows[i][0])
		if rows[i][0]==rows[i-1][0]:
			word = rows[i][0]
			L.insert(numrows,rows[i][1])
		if rows[i][0] != word:
			T.insert(numrows,[rows[i][0],rows[i][1]])

print(T)
print(L)
	# print(rows[1])
	# print(rows[2])
	

		

			