import csv
#from turtle import color
import matplotlib.pylab as plt
matches=[]
with open("matches.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        matches.append(row)
m=len(matches)
season=["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]
List=[]
for i in range(len(season)):
    a=[]
    a.append(season[i])
    a.append({})
    List.append(a)
l=1
for i in range(1,m):
    indx=0
    for j in range(len(season)):
        if matches[i][1]==season[j]:
            indx=j
            break
    team1,team2=matches[i][4],matches[i][5]
    if team1 in List[indx][1].keys():
        List[indx][1][team1]+=1
    else:
        List[indx][1][team1]=1
    if team2 in List[indx][1].keys():
        List[indx][1][team2]+=1
    else:
        List[indx][1][team2]=1
teams=[]
for i in range(len(List)):
    teams.extend(List[i][1].keys())
teams=list(sorted(set(teams)))

match_played=[]
# making a list of match played by all the teams in  a year
for i in range(len(season)):
    played=[]
    for j in range(len(teams)):
        if teams[j] in List[i][1].keys():
            played.append(List[i][1][teams[j]])
        else:
            played.append(0)
    match_played.append(played)

pos=list(range(10))
width=0.05
# Plotting the bars
arr=[[0 for i in range(13)] for i in range(10)]
for i in range(10):
    for j in range(13):
        arr[i][j]=match_played[i][j]
fig, ax = plt.subplots()#we need to changefigsize=(14, 7
teams_1=["CSK","DC","DD","GL","K11P","KTK","KKR","MI","PW","RR","RPS","RCB","SRH"]
plt.bar(teams_1,arr[0])
a=arr[0].copy()
plt.bar(teams_1,arr[1],bottom=a)
for i in range(13):
    a[i]+=arr[1][i]
plt.bar(teams_1,arr[2],bottom=a)
for i in range(13):
    a[i]+=arr[2][i]
plt.bar(teams_1,arr[3],bottom=a)
for i in range(13):
    a[i]+=arr[3][i]
plt.bar(teams_1,arr[4],bottom=a)
for i in range(13):
    a[i]+=arr[4][i]
plt.bar(teams_1,arr[5],bottom=a)
for i in range(13):
    a[i]+=arr[5][i]
plt.bar(teams_1,arr[6],bottom=a)
for i in range(13):
    a[i]+=arr[6][i]
plt.bar(teams_1,arr[7],bottom=a)
for i in range(13):
    a[i]+=arr[7][i]
plt.bar(teams_1,arr[8],bottom=a)
for i in range(13):
    a[i]+=arr[8][i]
plt.bar(teams_1,arr[9],bottom=a)
ax.set_ylabel('Number of matches')
ax.set_title('IPL Teams')
ax.set_xticklabels(teams_1)
plt.legend(season)

plt.show()
