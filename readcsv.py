from array import *
import csv

T = []
val1 = None
val2 = None
val3 = None
with open('gre-words-contextual-3.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	
	for row in readCSV:

		numrows = len(T)
		print(numrows)
		val1 = row[2]
		val2 = row[3]
		val3 = row[4]
		if val1 != '':
			
			T.insert(numrows, [row[0],row[1]])
			numrows = len(T)
			T.insert(numrows, [row[0],val1])
			if val2 != '':
				numrows = len(T)
				T.insert(numrows, [row[0],val2])
			if val3!= '':
				numrows = len(T)
				T.insert(numrows, [row[0],val3])
		else:
			numrows = len(T)
			T.insert(numrows, [row[0],row[1]])

for r in T:
    for c in r:
        print(c,end = " ")
    print()		

myFile = open('writeto-2.csv', 'w',newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(T)
     
print("Writing complete")
	
			

			