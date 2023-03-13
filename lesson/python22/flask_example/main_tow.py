import flask
import requests
from bs4 import BeautifulSoup
from flask import redirect, url_for

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'kekkekekek'



if __name__ == "__main__":
    app.run(debug=True)
