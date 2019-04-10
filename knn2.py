import csv
from operator import itemgetter
file=open("dataset.csv","r")
fileReader=csv.reader(file)
list=[]
flag=0
for row in fileReader:
	if(flag==0):
		flag=1

		continue	
	list.append(row)

pointX=5
pointY=3


for i in range(0,len(list)):

		list[i].append( pow((pointX-int(list[i][0])),2) +  pow((pointY-int(list[i][1])),2)  )

list=sorted(list,key=itemgetter(3))

for row in list:
	print(row)

k=3
o=0
b=0
for i in range(0,k):
	if(list[i][2]=="o"):
		o=o+1
	else:
		b=b+1

print("Classified as orange") if  o>b else print("Classified as blue")