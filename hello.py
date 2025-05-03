from flask import Flask, render_template
import helper as help
import json

app = Flask(__name__)

@app.route('/')
def index():
    businesses = help.getRestaurant('Indian', 'San Francisco', limit=1)

    help.storeRestaurantData(businesses, filename='yelp_data.json')

    businesses = help.readRestaurantData(filename='yelp_data.json')

    return render_template('index.html', businesses=businesses)