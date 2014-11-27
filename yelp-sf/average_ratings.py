#!/usr/bin/python

import pymongo
import numpy as np

def main():
    client = pymongo.MongoClient()
    db = client['yelp_db']

    records = {}
    for crime in db.restaurants.find():
        restaurants = crime['restaurants']
        ratings = [r['rating'] for r in restaurants]
        records[crime['incidentNum']] = np.mean(ratings)

if __name__ == '__main__':
    main()
