import helper as help
import json

def getHighestRatedRestaurant(limit=20):
    businesses = help.getRestaurant('restaurant', 'San Jose', limit=limit, sort_by='rating')
    help.storeRestaurantData(businesses, filename='data/data_by_rating.json')
    
    business_review_dict = {}
    for business in businesses:
        business_review_dict[business['name']] = {
            'rating': business['rating'],
            'review_count': business['review_count'],
            'price': business.get('price', 'N/A'),
            'location': business['location']['address1'],
            'phone': business.get('display_phone', 'N/A')
        }
    return business_review_dict

def getMostReviewedRestaurant(limit=20):
    businesses = help.getRestaurant('restaurant', 'San Jose', limit=limit, sort_by='review_count')
    help.storeRestaurantData(businesses, filename='data/data_by_review_count.json')
    
    business_review_dict = {}
    for business in businesses:
        business_review_dict[business['name']] = {
            'rating': business['rating'],
            'review_count': business['review_count'],
            'price': business.get('price', 'N/A'),
            'location': business['location']['address1'],
            'phone': business.get('display_phone', 'N/A')
        }
    return business_review_dict

def getMostPopularCategory():
    terms=['Indian',
            'Chinese',
            'Italian',
            'Mexican',
            'American',
            'Japanese',
            'Thai',
            'French',
            'Spanish',
            'Mediterranean',
            'Vietnamese',
            'Korean',
            'Greek',
            'Turkish',
            'Lebanese',
            'Brazilian',
            'Caribbean',
            'Cuban',
            'Hawaiian',
            'Filipino',
            'Russian',
            'Polish',
            'Swedish',
            'Norwegian',
            'Danish',
            'Finnish',
            'Icelandic',]
    category_dict = {}
    for term in terms:
        category_dict[term] = help.getTotalSearchResultByTerm(term, location='San Jose')

    category_dict = dict(sorted(category_dict.items(), key=lambda item: item[1], reverse=True))   
    
    # Store the category data in a JSON file
    with open('data/category_data.json', 'w') as f:
        json.dump(category_dict, f, indent=4)

    return category_dict