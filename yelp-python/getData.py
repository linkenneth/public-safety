# -*- coding: utf-8 -*-
"""
Yelp API v2.0 code sample.

This program demonstrates the capability of the Yelp API version 2.0
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Please refer to http://www.yelp.com/developers/documentation for the API documentation.

This program requires the Python oauth2 library, which you can install via:
`pip install -r requirements.txt`.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
import argparse
import json
import pprint
import sys
import urllib
import urllib2

import oauth2

import pandas as pd
#from pymongo import MongoClient

API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'food'
DEFAULT_LOCATION = 'SanFrancisco,CA'
SEARCH_LIMIT = 20
SORT = 1;
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = open('consumer_key.key').read().strip()
CONSUMER_SECRET = open('consumer_secret.key').read().strip()
TOKEN = open('token.key').read().strip()
TOKEN_SECRET = open('token_secret.key').read().strip()


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    encoded_params = urllib.urlencode(url_params)
    url = 'http://{0}{1}?{2}'.format(host, path, encoded_params)

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request('GET', url, url_params)
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': term,
        'll': location,
        'limit': SEARCH_LIMIT,
	'sort': SORT,
	'radius_filter': 4000
    }

    a = request(API_HOST, SEARCH_PATH, url_params=url_params)
    return a

def get_business(business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)

def query_api(term, location):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location)

    businesses = response.get('businesses')
    if not businesses:
        print 'No businesses for {0} in {1} found.'.format(term, location)
        return
    return businesses


#client = MongoClient()
#db = client['yelp_db']

path = "../sf-city-data/sfpd-reported-incidents-2003-to-present/"
name = "sfpd_incident_2003.csv"
fileloc = path + name
find = "food"
df = pd.read_csv(fileloc)
i = 0
for item in df.iterrows():
    i += 1
    if i > 150:
      break
    item = item[1]
    a = item.Y
    b = item.X
    loc = str(a) + ',' + str(b)
    result = query_api(find, loc)
    put = {"incidentNum": item.IncidntNum, "restaurants": result}
    print put
    #db.restaurants.insert(put)
    
