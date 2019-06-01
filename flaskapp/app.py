from flask import Flask, render_template, url_for, flash, redirect, request
from data import data

app = Flask(__name__)
app.secret_key = '12345678'


# Get foods without duplicates
foods = []
for view in data:
    if view['food'] in foods:
        continue
    foods.append(view['food'])


def get_views(food):
    views = []
    for view in data:
        if view['food'] == food:
            views.append(view)

    return views


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', foods=foods)


@app.route('/food/<food>')
def food(food):

    if food not in foods:
        flash(f'{food} not found', 'danger')
        return redirect(url_for('home'))

    return render_template('food.html', food=food, views=get_views(food))


if __name__ == '__main__':
    app.run(debug=True)
