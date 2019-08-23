from flask import Flask, render_template, url_for, abort, send_from_directory, request, flash, jsonify
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


@app.route('/get_data', methods=['POST'])
def get_data():
    file_number = request.form['value']
    data = list()
    items = list()

    with open(f'gtrends/geoMap{file_number}.csv', 'r') as f:
        csv = f.read().split('\n')
        for line in csv[3:]:
            data.append(line)

    for item in data:
        parts = item.split(',')
        if len(parts) > 1 and parts[1] != '':
            items.append({parts[0]: parts[1]})
        else:
            items.append({parts[0]: '1'})

    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)
