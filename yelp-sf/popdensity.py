import pandas as pd
import math
DATA_PATH = 'sfpd-reported-incidents-2003-to-present'
NAME_F = 'sfpd_incident_%d.csv'
YEARS = range(2003, 2014 + 1)  # 2003 to 2014, inclusive

data = {}
for year in YEARS:
    name = NAME_F % year
    data[year] = pd.read_csv('%s/%s' % (DATA_PATH, name))
holder = pd.read_csv("tract.csv")
turnup = holder[["TRACTCE10,C,6","INTPTLAT10,C,11","INTPTLON10,C,12"]]
turnup.head()
quavo = data[2014]
turnup.columns = ["Trace", "Y", "X"]
def distance(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc * 3396
def findTract(row,data):
    tempX = row["X"]
    tempY = row["Y"]
    temp = 100
    correct = None
    for index,row in data.iterrows():
        holder = distance(tempX,tempY,row["X"],row["Y"])
        if holder < temp:
            temp = holder
            correct = index
            
    return data.iloc[correct]["Trace"]

runner = quavo[:12000]
quartile = turnup.head()
whoadie = []
print len(runner)
for x in range(0,len(runner)):
    whoadie.append(findTract(runner.iloc[x],turnup))

# whos = {}
# for i, row in loc.iterrows():
#     print i, row['id']
#     whos[i] = findTract(row, turnup)
    
runner["Tract"] = whoadie
migosatl = pd.read_csv("population.csv")
atl = migosatl[["Tract2010,N,9,0","Pop_psmi,N,13,11"]]
atl.columns = ["Tract","PopDensity(sqmi)"]
dunny = runner.merge(atl,how="inner", on="Tract")
dunny.to_csv("12kpopdensity.csv")
