
import matplotlib
matplotlib.use("Agg")
from app import functions as f
import matplotlib.pyplot as plt
import numpy as np



# function to plot the highest rated restaurant
def plot_highest_rated_restaurant(limit=3):
    # Get the highest rated restaurant data
    highest_rated_restaurant = f.getHighestRatedRestaurant(limit)

    restaurant_names = []
    ratings = []
    # Extract restaurant names and ratings
    for restaurant in highest_rated_restaurant:
        restaurant_names.append(restaurant['name'])
        ratings.append(restaurant['rating'])    

    restaurant_names = np.array(restaurant_names)
    ratings = np.array(ratings)

    plt.bar(restaurant_names, ratings, color='blue')

    plt.xlabel('Restaurant Name')
    plt.ylabel('Rating')
    plt.title('Highest Rated Restaurants')
    plt.savefig('app/static/highest_rated_restaurants.png')
    plt.close()

def plot_most_reviewed_restaurant(limit=3):
    # Get the most reviewed restaurant data
    most_reviewed_restaurant = f.getMostReviewedRestaurant(limit)

    restaurant_names = []
    review_counts = []
    # Extract restaurant names and ratings
    for restaurant in most_reviewed_restaurant:
        restaurant_names.append(restaurant['name'])
        review_counts.append(restaurant['rating'])    

    restaurant_names = np.array(restaurant_names)
    review_counts = np.array(review_counts)

    plt.bar(restaurant_names, review_counts, color='green')

    plt.xlabel('Restaurant Name')
    plt.ylabel('Review Count')
    plt.title('Most Reviewed Restaurants')

    plt.savefig('app/static/most_reviewed_restaurants.png')
    plt.close()

def plot_highest_rated_cuisine(limit=3):
    # Get the highest rated cuisine data
    highest_rated_cuisine = f.getMostPopularCategory(limit)

    # Extract cuisine names and ratings
    cuisine_names = []
    ratings = []
    # Extract restaurant names and ratings
    for restaurant in highest_rated_cuisine:
        cuisine_names.append(restaurant['term'])
        ratings.append(restaurant['total'])    

    cuisine_names = np.array(cuisine_names)
    ratings = np.array(ratings)

    plt.bar(cuisine_names, ratings, color='red')

    plt.xlabel('Cuisine Name')
    plt.ylabel('Rating')
    plt.title('Highest Rated Cuisines')

    plt.savefig('app/static/highest_rated_cuisines.png')
    plt.close()
    