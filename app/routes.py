from flask import render_template, url_for, request
from app import app
from app import functions as f
from app import visualizer as v

# f.fetchAndStore()

#Rate endpoints
@app.route('/rate', methods=['GET'])
def rate():
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_highest_rated_restaurant(limit=limit)
    save_path = url_for('static', filename='highest_rated_restaurants.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='rate')

@app.route('/review', methods=['GET'])
def review():
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_most_reviewed_restaurant(limit=limit)
    save_path = url_for('static', filename='most_reviewed_restaurants.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='review')


@app.route('/cuisine', methods=['GET'])
def cuisine():
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_highest_rated_cuisine(limit=limit)
    save_path = url_for('static', filename='highest_rated_cuisines.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='cuisine')

if __name__ == '__main__':
    app.run()