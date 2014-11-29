#!/usr/bin/python

import pymongo
import numpy as np
import pandas as pd

def main():
    client = pymongo.MongoClient()
    db = client['yelp_db']

    records = {}
    for crime in db.restaurants.find():
        restaurants = crime['restaurants']
        ratings = [r['rating'] for r in restaurants]
        records[crime['incidentNum']] = np.mean(ratings)

    df = pd.DataFrame.from_dict(records, orient='index')
    df.to_csv('yelp_average_ratings.csv')

if __name__ == '__main__':
    main()
