from array import *
import csv
Topics = []
sublist = []
#slistcount = 0
numelements = 0
count = 0 
with open('tweakspeaking.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	for row in readCSV:
		if(row[0] != ''):
			#print (row[0])
			Topics.append(row[0])
			

		
		if count != 15 :
			
			sublist.append(row[1])
			
			count = count+1
			numelements = len(sublist)
			if numelements == 15:
				print(sublist)
				print("______________________________________________________________")
				
				with open("arraywrite.txt", "a") as output:
					output.write(str(sublist)+"\n\n")
			
		else:		
			sublist = []
			sublist.append(row[1])
			count = 0
			count = count+1
	print(Topics)
