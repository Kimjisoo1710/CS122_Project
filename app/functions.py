from app import helper as help
import json

def fetchAndStore():
    businesses = help.getRestaurant('restaurant', 'San Jose', limit=50, sort_by='rating')
    help.storeRestaurantData(businesses, filename='data/data_by_rating.json')
    businesses = help.getRestaurant('restaurant', 'San Jose', limit=50, sort_by='review_count')
    help.storeRestaurantData(businesses, filename='data/data_by_review_count.json')
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
    # category_dict = {}
    # for term in terms:
    #     category_dict[term] = help.getTotalSearchResultByTerm(term, location='San Jose')

    # category_dict = dict(sorted(category_dict.items(), key=lambda item: item[1], reverse=True))   

    category_arr=[]

    for term in terms:
        category_dict = {}
        category_dict['term'] = term
        category_dict['total'] = help.getTotalSearchResultByTerm(term, location='San Jose')
        category_arr.append(category_dict)
    
    # Sort the category data by total in descending order
    category_arr = sorted(category_arr, key=lambda x: x['total'], reverse=True)

    # Store the category data in a JSON file
    with open('data/category_data.json', 'w') as f:
        json.dump(category_arr, f, indent=4)
    

def getHighestRatedRestaurant(limit=20):
    businesses = help.readRestaurantData('data/data_by_rating.json') 

    # business_review_dict = {}
    # for business in businesses[:limit]:
    #     business_review_dict[business['name']] = {
    #         'rating': business['rating'],
    #         'review_count': business['review_count'],
    #         'price': business.get('price', 'N/A'),
    #         'location': business['location']['address1'],
    #         'phone': business.get('display_phone', 'N/A')
    #     }
    # return business_review_dict

    business_review_arr = []
    for business in businesses[:limit]:
        business_review_arr.append({
            'name': business['name'],
            'rating': business['rating'],
            'review_count': business['review_count'],
            'price': business.get('price', 'N/A'),
            'location': business['location']['address1'],
            'phone': business.get('display_phone', 'N/A')
        })
    return business_review_arr

def getMostReviewedRestaurant(limit=20):
    businesses = help.readRestaurantData('data/data_by_review_count.json')
    
    # business_review_dict = {}
    # for business in businesses[:limit]:
    #     business_review_dict[business['name']] = {
    #         'rating': business['rating'],
    #         'review_count': business['review_count'],
    #         'price': business.get('price', 'N/A'),
    #         'location': business['location']['address1'],
    #         'phone': business.get('display_phone', 'N/A')
    #     }
    # return business_review_dict

    business_review_arr = []
    for business in businesses[:limit]:
        business_review_arr.append({
            'name': business['name'],
            'rating': business['rating'],
            'review_count': business['review_count'],
            'price': business.get('price', 'N/A'),
            'location': business['location']['address1'],
            'phone': business.get('display_phone', 'N/A')
        })
    return business_review_arr

def getMostPopularCategory(limit=20):
    # Read the category data from the JSON file
    with open('data/category_data.json', 'r') as f:
        category_arr = json.load(f)

    return category_arr[:limit]


    