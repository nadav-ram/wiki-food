from flask import Flask, render_template, url_for, flash, redirect, request
from data import data as data

app = Flask(__name__)


@app.route('/')
def home():

    foods = []
    for view in data:
        if view['food'] in foods:
            continue
        foods.append(view['food'])

    return render_template('layout.html', foods=foods)


if __name__ == '__main__':
    app.run(debug=True)
