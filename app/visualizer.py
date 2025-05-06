import matplotlib
matplotlib.use("Agg")
from app import functions as f
import matplotlib.pyplot as plt
import numpy as np

def plot_highest_rated_restaurant(limit=3):
    # Fetch data
    data = f.getHighestRatedRestaurant(limit)
    names = [item['name'] for item in data]
    ratings = [item['rating'] for item in data]

    # Create a larger, horizontal bar chart
    plt.figure(figsize=(14, 8))
    bars = plt.barh(names, ratings, color='skyblue', edgecolor='grey')

    # Styling
    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Restaurant Name', fontsize=14)
    plt.title('Highest Rated Restaurants', fontsize=18)
    plt.gca().invert_yaxis()  # Highest at the top
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save
    plt.savefig('app/static/highest_rated_restaurants.png')
    plt.close()


def plot_most_reviewed_restaurant(limit=3):
    # Fetch data
    data = f.getMostReviewedRestaurant(limit)
    names = [item['name'] for item in data]
    counts = [item['review_count'] for item in data]

    # Create a larger, horizontal bar chart
    plt.figure(figsize=(14, 8))
    bars = plt.barh(names, counts, color='seagreen', edgecolor='grey')

    # Styling
    plt.xlabel('Review Count', fontsize=14)
    plt.ylabel('Restaurant Name', fontsize=14)
    plt.title('Most Reviewed Restaurants', fontsize=18)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save
    plt.savefig('app/static/most_reviewed_restaurants.png')
    plt.close()


def plot_highest_rated_cuisine(limit=3):
    # Fetch data
    data = f.getMostPopularCategory(limit)
    cuisines = [item['term'] for item in data]
    totals = [item['total'] for item in data]

    # Create a larger, horizontal bar chart
    plt.figure(figsize=(14, 8))
    bars = plt.barh(cuisines, totals, color='salmon', edgecolor='grey')

    # Styling
    plt.xlabel('Count', fontsize=14)
    plt.ylabel('Cuisine Name', fontsize=14)
    plt.title('Most Popular Cuisines', fontsize=18)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save
    plt.savefig('app/static/highest_rated_cuisines.png')
    plt.close()