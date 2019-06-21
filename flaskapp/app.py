from flask import Flask, render_template, url_for, abort, send_from_directory, request, flash
from data import data
from render_map import render_map

app = Flask(__name__)
app.secret_key = '12345678'
app.static_url_path = ''


# Get foods without duplicates
foods = {view['food'] for view in data}


# Return all views of a food
def get_views(food, year=None, month=None):
    if year == None and month == None:
        return [view for view in data if view['food'] == food]
    else:
        return [view for view in data if view['food'] == food and view['year'] == int(year) and view['month'] == int(month)]


# Home page
@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', foods=foods)
    elif request.method == 'POST':
        query = str(request.form['query']).lower()
        search_foods = {view['food'] for view in data if query in view['food']}
        return render_template('home.html', foods=search_foods, query=query)


# Single food page
@app.route('/food/<food>', methods=['GET', 'POST'])
def food(food):
    if food in foods:
        if request.method == 'GET':
            return render_template('food.html', food=food, views=get_views(food))
        if request.method == 'POST':
            year = request.form['year']
            month = request.form['month']
            day = request.form['day']
            if year == '' or int(year) <= 0 or month == '' or int(month) <= 0 or day == '' or int(day) <= 0:
                flash('Please provide a year, month and day', 'danger')
                return render_template('food.html', food=food, views=get_views(food))
            else:
                return render_template('food.html', food=food, views=get_views(food, year, month), year=year, month=month, day=day)
    else:
        abort(404)


# Render map file by food
@app.route('/render_map/<query>')
@app.route('/render_map/<query>/<year>/<month>/<day>')
def map(query, year=None, month=None, day=None):
    if query in foods:
        render_map(query, year, month, day)
        return send_from_directory('', 'gmplot.html')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
