import pandas as pd

DATA_PATH = 'sfpd-reported-incidents-2003-to-present'
NAME_F = 'sfpd_incident_%d.csv'
YEARS = range(2003, 2014 + 1)  # 2003 to 2014, inclusive

data = {}
for year in YEARS:
    name = NAME_F % year
    data[year] = pd.read_csv('%s/%s' % (DATA_PATH, name))

holder3 = pd.read_csv("yelp_average_ratings.csv")
holder3 = holder3.rename(columns = {"Unnamed: 0": "IncidntNum", "0":"Rating"})
close = pd.merge(data[2014], holder3, on="IncidntNum",how= 'inner')
necessary = close[["X","Y","Rating"]]
print necessary["Rating"].describe(percentiles = [.25,.5,.75,.85,.95])
#necessary.to_json("testies.json",orient="index")