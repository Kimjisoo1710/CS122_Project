from flask import render_template, url_for, request, redirect, session
from app import app
from app import functions as f
from app import visualizer as v

# f.fetchAndStore()
app.secret_key = 'replace-with-a-secure-random-value'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # if you’re submitting via <form method="POST">
        location = request.form.get('location', default='San Jose')
        # store in session
        session['location'] = location
        print(location)
        f.fetchAndStore(location=location)
        return redirect(url_for('rate'))
    # GET
    return render_template('welcome.html')


#Rate endpoints
@app.route('/rate', methods=['GET'])
def rate():
    location = session.get('location', 'San Jose')
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_highest_rated_restaurant(limit=limit)
    save_path = url_for('static', filename='highest_rated_restaurants.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='rate', location=location, criteria='rating', total_results = f.getTotalSearchResultByTerm('restaurant', location))

@app.route('/review', methods=['GET'])
def review():
    location = session.get('location', 'San Jose')
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_most_reviewed_restaurant(limit=limit)
    save_path = url_for('static', filename='most_reviewed_restaurants.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='review', location=location, criteria='review', total_results = f.getTotalSearchResultByTerm('restaurant', location))


@app.route('/cuisine', methods=['GET'])
def cuisine():
    location = session.get('location', 'San Jose')
    #plot the highest rated restaurant
    limit = request.args.get('limit', default=3, type=int)
    v.plot_highest_rated_cuisine(limit=limit)
    save_path = url_for('static', filename='highest_rated_cuisines.png')
    return render_template('index.html', save_path=save_path, limit=limit, action='cuisine', location=location, criteria='review')

if __name__ == '__main__':
    app.run()