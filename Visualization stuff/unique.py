import pandas as pd

holder2 = pd.read_csv("Ratings.csv")
holder3 = pd.read_csv("locations.csv")
close = pd.merge(holder2, holder3, on="id",how= 'inner')
necessary = close[["X","Y","rating"]]
print necessary["rating"].describe(percentiles = [.25,.5,.75,.85,.95])
necessary.to_json("frontin.json",orient="index")