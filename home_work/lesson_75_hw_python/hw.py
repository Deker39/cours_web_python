import flask
import requests
from bs4 import BeautifulSoup
from flask import redirect, url_for

app = flask.Flask(__name__)

# main, new city, City management, fact about city, contacts: tel city service

MENU_TITLE = ['main', 'news', 'management', 'facts', 'contacts', 'history']
CONTENT_NEWS = []
news_url = 'https://dumskaya.net/'
news_request = requests.get(news_url)
news_text = BeautifulSoup(news_request.text, "lxml")

[CONTENT_NEWS.append(news_text.find('tr', {'id': f'newstr{i}'}).text.split(" ,")) for i in range(1, 11)]

CONTENT_MANAGEMENT = {
    'mayor': 'Gennadiy Trukhanov',
    'flag': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Flag_of_Odessa.svg/150px-Flag_of_Odessa.svg.png',
    'coat of arms': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Coat_of_Arms_of_Odessa.svg/135px'
                    '-Coat_of_Arms_of_Odessa.svg.png',
    'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Odessa_logo.svg/105px-Odessa_logo.svg.png'
}
CONTENT_CONTACTS = [
    ['Fire department', '101'],
    ['Police', '102'],
    ['Ambulance ', '103'],
    ['Emergency gas service', '104'],
    ['Operational city center "Ambulance communal assistance"', '15-01 , (048) 755-00-50'],
    ['JSC DTEK "Odesa Electric Grids"', '+38 (068) 750 90 90'],
    ['JSC "ODESAGAZ"', '705-39-09'],
    ['Infoxvodokanal branch', '0-800-307-505'],
    ['KP "Heat supply of the city of Odessa"', '705-62-18,'],
    ['Odeslift branch,', '(048) 717-45-31'],
    ['KP "Odesmisksvitlo"', '(048) 735-81-60']
]
CONTENT_FACTS = [
    ['In the tower of house # 5 on Preobrazhenskaya Street there is a Constructed Odessa Lighthouse, which works “in '
     'pairs” with Vorontsovsky and assists ships entering the port. If the ship is on the right course, '
     'then both beacons on the course line can be viewed simultaneously visually one above the other. Thanks to the '
     'difference in the height of the characters, you can clearly determine which direction to adjust the course. The '
     'height of the beacon above sea level is 54.9 meters.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/51121583492404874.jpg'],
    ['In Odessa there is a street named after the twin city – Genoa. And in the Italian Genoa, in turn, there is a '
     'street Odessa – Via Odessa. Genoa is also on the Twin Cities signpost near Duma Square: 1706 kilometers to it.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/44121583493448887.jpg'],
    ['From 1845, Franz Morandi, the Italian, was the chief architect of Odessa: he created a synagogue at the corner '
     'of Richelieu and Jewish, developed a master plan for the city, expanded Alexander Avenue, and oversaw the '
     'construction and decoration of the Roman Catholic cathedral at Catherine. In addition, his authorship is owned '
     'by many houses on Kanatnaya, Trinity, Richelieu, Primorsky Boulevard, Polish Street, Kateryna Square, '
     'Marazlievskaya, Pushkin, Langeronovskaya, Uspenskaya and so on.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/18711583494847018.jpg'],
    ['In the Odessa Archaeological Museum is stored the gold coin of Prince Vladymir – the first gold coin of Kyivan '
     'Rus, minted at the end of XX beginning of XI century. There are only 11 in the world: in the Hermitage – 7 in '
     'the Russian State History Museum – 1 in the National Museum of History of Ukraine – 1 and the location of '
     'another one is unknown.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/61451583495434725.jpg'],
    ['Sergiy Pankyev’s story has become one of Freud’s five major clinical cases. At an early age, he suffered from '
     'zoophobia (and at the same time wanted to torture animals), nightmarish obsessions. It was in this house that '
     'he had a terrible dream of white wolves, silently sitting on the branches of a tree and sending him a message '
     'through his eyes. Since then, Pankeev considered himself a wolf for the rest of his life.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/92751583495926808.jpg'],
    ['To see it you need to look at the corner house in Catherine and Greek. The balcony completely frames the '
     'building without interruption. This is the so-called Mavrocordato apartment building built in 1905 by architect '
     'Yuriy Dmitrenko.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/84831583496196967.jpg'],
    ['The monument was created by the famous Odessa artist Alexander Milov. And earlier on this place was a monument '
     'to Lenin, which was to be dismantled in the framework of decommunization. Lenin was not demolished, '
     'suddenly someone else would come in handy – the Vader sculpture was “put on” by him.',
     'https://ek.stripocdn.email/content/guids/CABINET_24d49a97b4fb43d3a57b4cbe5c638a3a/images/75261583496479792.jpg']
]


@app.route('/')
@app.route('/main')
def main():
    context = {
        'menu': MENU_TITLE,
        'context': [
            {
                'title': 'facts',
                'content': CONTENT_FACTS
            },
            {
                'title': 'news',
                'content': CONTENT_NEWS
            },
            {
                'title': 'management',
                'content': CONTENT_MANAGEMENT
            },
            {
                'title': 'contacts',
                'content': CONTENT_CONTACTS
            }
        ]
    }
    return flask.render_template('main.html', context=context)


@app.route('/news')
def news():
    context = {
        'title': 'news',
        'menu': MENU_TITLE,
        'content': CONTENT_NEWS
    }
    return flask.render_template('news.html', context=context)


@app.route('/news/<any>')
def new_news(any):
    return news()


@app.route('/management')
def management():
    context = {
        'title': 'management',
        'menu': MENU_TITLE,
        'content': CONTENT_MANAGEMENT
    }
    return flask.render_template('management.html', context=context)


@app.route('/management/<any>')
def new_management(any):
    return management()


@app.route('/facts')
def fact():
    context = {
        'title': 'facts',
        'menu': MENU_TITLE,
        'content': CONTENT_FACTS
    }
    return flask.render_template('fact.html', context=context)


@app.route('/facts/<any>')
def new_fact(any):
    return fact()


@app.route('/contacts')
def contacts():
    context = {
        'title': 'contacts',
        'menu': MENU_TITLE,
        'content': CONTENT_CONTACTS
    }
    return flask.render_template('contacts.html', context=context)


@app.route('/contacts/<any>')
def new_contacts(any):
    return contacts()


@app.route('/history')
def history():
    context = {
        'title': 'history',
        'menu': MENU_TITLE,
        'content': 'history'
    }
    return flask.render_template('history.html', context=context)


@app.route('/history/people')
def people():
    context = {
        'title': 'people',
        'menu': MENU_TITLE,
        'content': 'people'
    }
    return flask.render_template('people.html', context=context)


@app.route('/history/photo')
def photos():
    context = {
        'title': 'photo',
        'menu': MENU_TITLE,
        'content': 'photos'
    }
    return flask.render_template('photos.html', context=context)




# @app.errorhandler(404)
# def page_not_found(e):
#     print(app)
#     return redirect(url_for('news'))

if __name__ == "__main__":
    app.run(debug=True)
