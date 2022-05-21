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
m=len(matches)
mat=set()
for i in range(1,m):
    mat.add(matches[i][1])
season=list(sorted(mat))
List=[]
for i in range(len(season)):
    a=[]
    a.append(season[i])
    a.append({})
    List.append(a)
for i in range(1,m):
    indx=0
    for j in range(len(season)):
        if matches[i][1]==season[j]:
            indx=j
            break
    a,b=matches[i][4],matches[i][5]
    if a in List[indx][1].keys():
        List[indx][1][a]+=1
    else:
        List[indx][1][a]=1
    if b in List[indx][1].keys():
        List[indx][1][b]+=1
    else:
        List[indx][1][b]=1
teams=[]
for i in range(len(List)):
    teams.extend(List[i][1].keys())
teams=list(sorted(set(teams)))
match_played=[]
for i in range(len(season)):
    played=[]
    for j in range(len(teams)):
        if teams[j] in List[i][1].keys():
            played.append(List[i][1][teams[j]])
        else:
            played.append(0)
    match_played.append(played)
for i in range(len(season)):
    if i==0:
        plt.bar(teams,match_played[i],0.2)
    else:
        plt.bar(teams,match_played[i],0.2,bottom=match_played[i-1])

plt.legend(season)
plt.grid()

plt.show()




    
    
       


    







