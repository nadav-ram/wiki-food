from flask import Flask, render_template, url_for, flash, redirect, request
from data import data

app = Flask(__name__)




if __name__ == '__main__':
    app.run(debug=True)