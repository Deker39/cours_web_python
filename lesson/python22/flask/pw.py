import random
from datetime import datetime

from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template('pw.html')

@app.route('/helloworld')
def hello():
    return '<h1>Hello World</h1>'

@app.route('/weekday')
def week_day():
    day =  datetime.today().isoweekday()
    weekdays = {1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"}
    return f'<h1>Today day is: {weekdays[day]}</h1>'

@app.route('/quotes')
def quotes():
    quotes = ['quotes1', 'quotes2', 'quotes3', 'quotes4', 'quotes5', 'quotes6']
    return f'<h1>{quotes[random.randint(0,len(quotes))]}</h1>'

if __name__ == '__main__':
    app.run(debug=True)