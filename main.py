from yelpapi import YelpAPI
import argparse
from pprint import pprint
import pandas as pd
import os
from os import getenv, getcwd

# API = "2cEuTjdY1ANznuTbvaN6v7i-uIZxSGyERue_wOd-C61iQeuQGN6TW_aDnoy_BZQPbRrTWK2MIg_aFR9F60A3-EJ--izJc_0hi9TvHNp_UcWW0YF9Ra88hJI6_zuXX3Yx"

API = getenv("API")

yelp_api = YelpAPI(API)

# Pull list of phone numbers and restaurant names from gSheets 

# Search for business IDs from above list

# Transform business IDs data and load into SQL table

# Search for reviews from above list

# Transform review data and load into SQL table


number = "+13193375512"

response = yelp_api.phone_search_query(phone=number)
pprint(response)

# reviews = response.get("reviews")

# df = pd.json_normalize(reviews)

# print(df)

# for review in reviews:
#     print(review.get("text"))