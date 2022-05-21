import csv
import matplotlib.pylab as plt
data=[]
with open("matches.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data.append(row)
UMPIRE_COUNTRY = {
    'JD Cloete': 'south africa',
    'PR Reiffel': 'australia',
    'SJA Taufel': 'australia',
    'NJ Llong': 'england',
    'RK Illingworth': 'england',
    'GAV Baxter': 'New Zealand',
    'BG Jerling': 'south africa',
    'BR Doctrove': 'Dominican',
    'DJ Harper': 'American',
    'M Erasmus': 'south africa',
    'RB Tiffin': 'Zimbabwe',
    'CB Gaffaney': 'New Zealand',
    'MR Benson': 'england',
    'Aleem Dar': 'Pakistan',
    'SD Fry': 'australia',
    'AL Hill': 'New Zealand',
    'BF Bowden': 'New Zealand',
    'Asad Rauf': 'Pakistan',
    'TH Wijewardene': 'Sri Lanka',
    'BNJ Oxenford': 'australia',
    'IL Howell': 'south africa',
    'RE Koertzen': 'south africa',
    }

Dict={}
n=len(data)
ump=set()
ump1=set()
for i in range(2,n):
    ump.add(data[i][15])
    ump.add(data[i][16])
for i in ump:
    if(UMPIRE_COUNTRY.get(i)):
        if i not in ump1:
            if UMPIRE_COUNTRY[i] in Dict.keys():
                Dict[UMPIRE_COUNTRY[i]]+=1
            else:
                Dict[UMPIRE_COUNTRY[i]]=1

country=[]
umpire=[]
for i in Dict.keys():
    country.append(i)
    umpire.append(Dict[i])
plt.barh(country,umpire)
plt.show()
    
