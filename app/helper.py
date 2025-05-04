from yelpapi import YelpAPI
import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

api_key = os.getenv('API_KEY')

yelp_api = YelpAPI(api_key)  # Replace with your actual Yelp API key

BASE_DIR = Path(__file__).resolve().parent    # …/CS122_Project
DATA_DIR = BASE_DIR 
DATA_DIR.mkdir(parents=True, exist_ok=True)

def get(term, location, limit=20, offset=0, sort_by='best_match'):
    response = yelp_api.search_query(term=term, location=location, limit=limit, offset=offset, sort_by=sort_by)
    return response


def getRestaurant(term, location, limit=20, offset=0, sort_by='best_match'):
    # Get restaurant data from Yelp API
    response = yelp_api.search_query(term=term, location=location, limit=limit, offset=offset, sort_by=sort_by)
    return response['businesses']

def storeRestaurantData(businesses, filename):    
    filename = DATA_DIR / filename
    # Create a DataFrame from the list of businesses
    df = pd.DataFrame(businesses)

    # Write the DataFrame to a CSV file
    df.to_json(filename, orient='records', lines=True)

def readRestaurantData(filename):
    filename = DATA_DIR / filename
    # Read restaurant data from a CSV file
    df = pd.read_json(filename, orient='records', lines=True)
    return df.to_dict(orient='records')

def getTotalSearchResultByTerm(term, location='San Jose'):
    response = yelp_api.search_query(term=term, location=location, limit=1)
    return response['total']