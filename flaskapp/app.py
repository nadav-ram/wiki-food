from flask import Flask, render_template, url_for, flash, redirect, request, abort, send_from_directory
from data import data
from render_map import render_map

app = Flask(__name__)
app.secret_key = '12345678'
app.static_url_path = ''


# Get foods without duplicates
foods = {view['food'] for view in data}


# Return all views of a food
def get_views(food):
    return [view for view in data if view['food'] == food]


# Home page
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', foods=foods)


# Single food page
@app.route('/food/<food>')
def food(food):
    if food in foods:
        return render_template('food.html', food=food, views=get_views(food))
    else:
        abort(404)


# Render map by food
@app.route('/render_map/<query>')
def map(query):
    render_map(query)
    return send_from_directory('', 'gmplot.html')


if __name__ == '__main__':
    app.run(debug=True)
