import re
from datetime import datetime

from flask import *

app = Flask(__name__)

weekdays = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
            }
MENU_TITLE = ['love song', 'car', 'day weeks', 'headphones']
CONTENT_LOVE_SONG_EN = {'song': '«We are the champions, my friends And we\'ll keep on fighting till the end»',
                        'executor': 'Queen',
                        'name': 'We are the champions',
                        'lang': ['en', 'fr', 'de', 'es']
                        }
CONTENT_LOVE_SONG_FR = {'song': '«Nous sommes les champions, mes amis et nous continuerons à nous battre jusqu\'à la '
                                'fin»',
                        'executor': 'Queen',
                        'name': 'Nous sommes les champions',
                        'lang': ['en', 'fr', 'de', 'es']
                        }
CONTENT_LOVE_SONG_DE = {'song': '«Wir sind die Champions, meine Freunde, und wir werden bis zum Ende weiterkämpfen»',
                        'executor': 'Queen',
                        'name': 'Wir sind die Gewinner',
                        'lang': ['en', 'fr', 'de', 'es']
                        }
CONTENT_LOVE_SONG_ES = {'song': '«Somos los campeones amigos y seguiremos luchando hasta el final»',
                        'executor': 'Queen',
                        'name': 'Nosotras somos las campeonas',
                        'lang': ['en', 'fr', 'de', 'es']
                        }
CONTENT_TOYOTA = [
    {
        'model': 'toyota',
        'description': 'Седан Corolla вперше представлено у гібридній варіації. Автомобіль напрочуд швидкий та '
                       'спритний завдяки застосуванню інноваційного самозарядного гібридного двигуна. Інженери '
                       'запровадили абсолютно новий підхід до дизайну та проєктування. Завдяки цьому найбільш '
                       'продавана модель у світі відтепер має нові характеристики: витончений екстер’єр, '
                       'повністю оновлений інтер’єр, низку удосконалених технологій та, що найважливіше, '
                       'поліпшені функції безпеки. Седан Corolla повертається – відтепер він ще кращий. ',
        'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWNA7cARZYqpPsGygfe8mrJ7_ZG4AX2izlog&usqp=CAU'
    }
]
CONTENT_HONDA = [
    {
        'model': 'honda',
        'description': 'Седан Corolla вперше представлено у гібридній варіації. Автомобіль напрочуд швидкий та '
                       'спритний завдяки застосуванню інноваційного самозарядного гібридного двигуна. Інженери '
                       'запровадили абсолютно новий підхід до дизайну та проєктування. Завдяки цьому найбільш '
                       'продавана модель у світі відтепер має нові характеристики: витончений екстер’єр, '
                       'повністю оновлений інтер’єр, низку удосконалених технологій та, що найважливіше, '
                       'поліпшені функції безпеки. Седан Corolla повертається – відтепер він ще кращий. ',
        'photo': 'https://honda-kiev.com.ua/uploads/media/dc_car_gallery/0001/23/thumb_22975_dc_car_gallery_new_slider.jpeg.webp'
    }
]
CONTENT_RENAULT = [
    {
        'model': 'renault',
        'description': 'Седан Corolla вперше представлено у гібридній варіації. Автомобіль напрочуд швидкий та '
                       'спритний завдяки застосуванню інноваційного самозарядного гібридного двигуна. Інженери '
                       'запровадили абсолютно новий підхід до дизайну та проєктування. Завдяки цьому найбільш '
                       'продавана модель у світі відтепер має нові характеристики: витончений екстер’єр, '
                       'повністю оновлений інтер’єр, низку удосконалених технологій та, що найважливіше, '
                       'поліпшені функції безпеки. Седан Corolla повертається – відтепер він ще кращий. ',
        'photo': 'https://www.evanshalshaw.com/-/media/evanshalshaw/renault/car-models/arkana/renault-arkana-driving-720x405px.ashx?mh=1440&la=en&h=405&w=720&mw=2560&hash=350DE90F2533AE72DEC244FD9C9B0084'
    }
]


RegEx = {
    'love_song': '^http:\/\/127\.0\.0\.1:5000\/love%20song.*$',
    'car': '^http:\/\/127\.0\.0\.1:5000\/car.*$',
    'day_weeks': '^http:\/\/127\.0\.0\.1:5000\/day%20weeks.*$',
    'headphones': '^http:\/\/127\.0\.0\.1:5000\/headphones.*$',
}


@app.route('/')
def index():
    context = {
        'title': 'main',
        'menu': MENU_TITLE,
        'content': ''
    }
    return render_template("main.html", context=context)


@app.route('/love song')
def love_song():
    context = {
        'title': 'love song',
        'menu': MENU_TITLE,
        'content': CONTENT_LOVE_SONG_EN
    }
    return render_template("love_song.html", context=context)


@app.route('/love song/<path:path>')
def love_song_en(path='en'):
    if path == 'en' or path == 'love song':
        return redirect('/love song')
    elif path == 'fr':
        context = {
            'title': 'chanson d\'amour',
            'menu': MENU_TITLE,
            'content': CONTENT_LOVE_SONG_FR
        }
        return render_template("love_song.html", context=context)
    elif path == 'de':
        context = {
            'title': 'Liebeslied',
            'menu': MENU_TITLE,
            'content': CONTENT_LOVE_SONG_DE
        }
        return render_template("love_song.html", context=context)
    elif path == 'es':
        context = {
            'title': 'canción de amor',
            'menu': MENU_TITLE,
            'content': CONTENT_LOVE_SONG_ES
        }
        return render_template("love_song.html", context=context)
    else:
        return redirect(f'/{path}')


@app.route('/car')
def car():
    context = {
        'title': 'car',
        'menu': MENU_TITLE,
        'type': ['toyota', 'honda', 'renault']

    }
    return render_template("car.html", context=context)


@app.route('/car/<path:path>')
def car_path(path):
    if path == 'toyota':
        context = {
            'title': 'car',
            'menu': MENU_TITLE,
            'type': ['toyota', 'honda', 'renault'],
            'content': CONTENT_TOYOTA
        }
        return render_template("car.html", context=context)
    elif path == 'honda':
        context = {
            'title': 'car',
            'menu': MENU_TITLE,
            'type': ['toyota', 'honda', 'renault'],
            'content': CONTENT_HONDA
        }
        return render_template("car.html", context=context)
    elif path == 'renault':
        context = {
            'title': 'car',
            'menu': MENU_TITLE,
            'type': ['toyota', 'honda', 'renault'],
            'content': CONTENT_RENAULT
        }
        return render_template("car.html", context=context)
    else:
        return redirect(f'/{path}')


@app.route('/day weeks')
def week_day():
    day = datetime.today().isoweekday()
    context = {
        'title': 'day weeks',
        'menu': MENU_TITLE,
        'weekdays': weekdays[day]
    }

    return render_template('day_week.html', context=context)


# @app.route('/headphones')
# def headphones():
#     context = {
#         'title': 'headphones',
#         'menu': MENU_TITLE,
#         'content': 'headphones'
#     }
#
#     return render_template('headphones.html', context=context)


@app.route('/headphones', method='GET')
def headphones():
    model = request.args.get('model')
    # if headphones_model == 'airpods':
    context = {
        'title': 'headphones',
        'menu': MENU_TITLE,
        'content': model
    }

    return render_template('headphones.html', context=context)




# @app.errorhandler(404)
# def page_not_found(e):
#     url = str(request.url)
#
#     if re.search(RegEx['love_song'], url) is not None:
#         return redirect(url_for('love_song_en'))
#     if re.search(RegEx['car'], url) is not None:
#         return redirect(url_for('car'))
#     if re.search(RegEx['day_weeks'], url) is not None:
#         return redirect(url_for('week_day'))
    # if re.search(RegEx['headphones'], url) is not None:
    #     return redirect(url_for('week_day'))


if __name__ == "__main__":
    app.run(debug=True)
