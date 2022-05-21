import csv
import matplotlib.pylab as plt
matches=[]
deleveries=[]
with open("matches.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        matches.append(row)
with open("deliveries.csv","r") as csvfile:
    reader_variable=csv.reader(csvfile,delimiter=",")
    for row in reader_variable:
        deleveries.append(row)
Dict={}
#for i in range(len(deleveries[0])):
 #   print(deleveries[0][i])

n=len(deleveries)
for i in range(1,n):
    if(deleveries[i][2]=="Royal Challengers Bangalore"):
        if(deleveries[i][6] in Dict.keys()):
            Dict[deleveries[i][6]]+=int(deleveries[i][-6])
        else:
        #print(deleveries[i][6])
            Dict[deleveries[i][6]]=int(deleveries[i][-6])
x=[]
y=[]
for i in Dict.keys():
    if(Dict[i]>=100):
        x.append(i)
        y.append(Dict[i])
plt.barh(x,y)
plt.show()
