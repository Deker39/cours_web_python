import re

import flask
import requests
from bs4 import BeautifulSoup
from flask import redirect, url_for, request

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
CONTENT_HISTORY = 'Odesa, also spelled Odessa, seaport, southwestern Ukraine. It stands on a shallow indentation of the' \
                  'Black Sea coast at a point approximately 19 miles (31 km) north of the Dniester River estuary and ' \
                  'about 275 miles (443 km) south of Kyiv.' \
                  'Although a settlement existed on the site in ancient times, the history of the modern city began ' \
                  'in the 14th century when the Tatar fortress of Khadzhibey was established there; it later passed ' \
                  'to Lithuania-Poland and in 1480 to Turkey. The fortress was stormed by the Russians in 1789 and ' \
                  'the territory ceded to Russia in 1792. A new fortress was built in 1792–93, and in 1794 a naval ' \
                  'base and commercial quay were added. In 1795 the new port was named Odesa for the ancient Greek ' \
                  'colony of Odessos, the site of which was believed to be in the vicinity.'
CONTENT_PEOPLE = [
    {
        'name': 'Yakov Smirnoff',
        'description': 'Yakov Smirnoff was born on January 24, 1951 in Odessa, Ukrainian SSR, USSR [now Ukraine]. He '
                       'is an actor and writer, known for Ночной суд (1984), Приключения Бак...',
        'photo': 'https://m.media-amazon.com/images/M'
                 '/MV5BMWRmNmZkNjgtYzEwMC00NjYyLTkzOTYtYzQ3ZjZiYWJmNGQ0XkEyXkFqcGdeQXVyMzA5NTMzNA@@._V1_UX140_CR0,0,'
                 '140,209_AL_.jpg'
    },
    {
        'name': 'Natasha Yarovenko',
        'description': 'Natasha Yarovenko was born on July 23, 1979 in Odessa, Ukrainian SSR, USSR [now Ukraine]. She '
                       'is an actress, known for Комната в Риме (2010), Афтершок (2012) and Дн&...',
        'photo': 'https://m.media-amazon.com/images/M/MV5BMzU5MTEwMTQyNV5BMl5BanBnXkFtZTcwNzU2Nzg0NA@@._V1_UY209_CR7,'
                 '0,140,209_AL_.jpg'
    },
    {
        'name': 'Natasha Blasick',
        'description': 'Natasha Blasick was born in the city of Odessa, Ukraine on the Black Sea. Her first languages '
                       'are Russian and Ukrainian. She grew up in a Soviet-style apartment that housed two families. '
                       'She made her debut as a lead actress in the film Death of Evil (2009). She is the older '
                       'daughter of Sergei and ...',
        'photo': 'https://m.media-amazon.com/images/M'
                 '/MV5BYjRiYzA5NDAtYjQwZC00YTUzLWIxM2EtMGU4YTA4MzA1ZDcyXkEyXkFqcGdeQXVyMTUwNDA5ODE@._V1_UX140_CR0,0,'
                 '140,209_AL_.jpg'
    },
    {
        'name': ' Lucian Pintilie',
        'description': 'Lucian Pintilie was born on November 9, 1933 in Tarutino, Bessarabia, Romania [now Tarutyne, '
                       'Odessa Oblast, Ukraine]. He was a director and writer, known for Конечная остановка - ра&...',
        'photo': 'https://m.media-amazon.com/images/M'
                 '/MV5BMDBiNmViYzEtOTI3Ni00ZDUxLWE1NWItNDg5YzNhNDgzZTA4XkEyXkFqcGdeQXVyMTc4MzI2NQ@@._V1_UY209_CR126,'
                 '0,140,209_AL_.jpg'
    },
    {
        'name': ' Val Chmerkovskiy',
        'description': 'Valentin Chmerkovskiy is a Ukrainian-born professional dancer, author and television '
                       'personality. A 14-time US National Champion and two-time World Dance Champion, Val rose to '
                       'stardom as a fan-favorite professional and eventual two-time winner of the hit series Dancing '
                       'with the Stars. He has since ...',
        'photo': 'https://m.media-amazon.com/images/M'
                 '/MV5BNGFhZTM1NDYtODkxOS00Yjk5LTg3NDAtZDJmODhmODhkNmQ4XkEyXkFqcGdeQXVyMTA1MDI3NjUy._V1_UX140_CR0,0,'
                 '140,209_AL_.jpg'
    },

]
CONTENT_PHOTO = [
    'https://plus.unsplash.com/premium_photo-1669131388677-1410dbaf8165?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8MXx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1614674664304-daaf7dee7aac?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8NXx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1620380593388-b36ea64e19ba?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1622057089684-5fd7008f5d50?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8NHx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://plus.unsplash.com/premium_photo-1669762078420-3c2a7d48aca5?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8N3x8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1622630781360-e79efc9980f8?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1613557841882-db2d6389dc3c?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8M3x8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://images.unsplash.com/photo-1587373291505-2637d492f715?ixlib=rb-4.0.3&ixid'
    '=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fG9kZXNzYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60'
]
RegEx = {
    'main': '^http:\/\/127\.0\.0\.1:5000\/main.*$',
    'news': '^http:\/\/127\.0\.0\.1:5000\/news.*$',
    'management': '^http:\/\/127\.0\.0\.1:5000\/management.*$',
    'facts': '^http:\/\/127\.0\.0\.1:5000\/facts.*$',
    'contacts': '^http:\/\/127\.0\.0\.1:5000\/contacts.*$',
    'history': '^http:\/\/127\.0\.0\.1:5000\/history.*$',
    'history_people': '^http:\/\/127\.0\.0\.1:5000\/history\/people.*$',
    'history_photo': '^http:\/\/127\.0\.0\.1:5000\/history\/photo.*$',

}


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
                'title': 'history',
                'content': CONTENT_HISTORY
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


@app.route('/management')
def management():
    context = {
        'title': 'management',
        'menu': MENU_TITLE,
        'content': CONTENT_MANAGEMENT
    }
    return flask.render_template('management.html', context=context)


@app.route('/facts')
def facts():
    context = {
        'title': 'facts',
        'menu': MENU_TITLE,
        'content': CONTENT_FACTS
    }
    return flask.render_template('fact.html', context=context)


@app.route('/contacts')
def contacts():
    context = {
        'title': 'contacts',
        'menu': MENU_TITLE,
        'content': CONTENT_CONTACTS
    }
    return flask.render_template('contacts.html', context=context)


@app.route('/history')
def history():
    context = {
        'title': 'history',
        'menu': MENU_TITLE,
        'content': CONTENT_HISTORY
    }
    return flask.render_template('history.html', context=context)


@app.route('/history/people')
def people():
    context = {
        'title': 'people',
        'menu': MENU_TITLE,
        'content': CONTENT_PEOPLE
    }
    return flask.render_template('people.html', context=context)


@app.route('/history/photo')
def photos():
    context = {
        'title': 'photo',
        'menu': MENU_TITLE,
        'content': CONTENT_PHOTO
    }
    return flask.render_template('photos.html', context=context)


@app.errorhandler(404)
def page_not_found(e):
    url = str(request.url)

    if re.search(RegEx['news'], url) is not None:
        return flask.redirect(url_for('news'))
    elif re.search(RegEx['management'], url) is not None:
        return flask.redirect(url_for('management'))
    elif re.search(RegEx['contacts'], url) is not None:
        return flask.redirect(url_for('contacts'))
    elif re.search(RegEx['history'], url) is not None:
        return flask.redirect(url_for('history'))
    elif re.search(RegEx['facts'], url) is not None:
        return flask.redirect(url_for('facts'))
    elif re.search(RegEx['people'], url) is not None:
        return flask.redirect(url_for('people'))
    elif re.search(RegEx['photo'], url) is not None:
        return flask.redirect(url_for('photo'))
    else:
        return flask.redirect('main.html')


if __name__ == "__main__":
    app.run(debug=True)
