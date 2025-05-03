from yelpapi import YelpAPI
import pandas as pd

yelp_api = YelpAPI('OwkJSQp-0rHEHHHDrWM74956yE9Ym1y9fSPg3lB5_FqDMKs2tP5oR-G5tkAm9tcr9ewSE88rhZqKMqSQ-sdi7GDlFiYzG_CWX3EACi249sr9VxkWb3zs4yB6gKsVaHYx')

def getRestaurant(term, location, limit=20, offset=0, sort_by='best_match'):
    # Get restaurant data from Yelp API
    response = yelp_api.search_query(term=term, location=location, limit=limit, offset=offset, sort_by=sort_by)
    return response['businesses']

def storeRestaurantData(businesses, filename='yelp_data.json'):    
    # Create a DataFrame from the list of businesses
    df = pd.DataFrame(businesses)

    # Write the DataFrame to a CSV file
    df.to_json(filename, orient='records', lines=True)

def readRestaurantData(filename='yelp_data.json'):
    # Read restaurant data from a CSV file
    df = pd.read_json(filename, orient='records', lines=True)
    return df.to_dict(orient='records')

def getTotalSearchResultByTerm(term, location='San Jose'):
    response = yelp_api.search_query(term=term, location=location, limit=1)
    return response['total']