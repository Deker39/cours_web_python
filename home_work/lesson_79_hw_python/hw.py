import os

from flask import Flask, render_template, request, redirect, url_for, json, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:26091998Asd@localhost/db"
app.config['SECRET_KEY'] = os.urandom(12)
db = SQLAlchemy(app)

menu = ['phone book', 'show']


class ModelPhoBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    mail = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    note = db.Column(db.String(80), nullable=False)


# class PhoBook:

    # def __init__(self, name, surname, mail, phone, note):
    #     self.note = note
    #     self.phone = phone
    #     self.mail = mail
    #     self.surname = surname
    #     self.name = name


# list_PhoBook = [PhoBook('alex', 'hol', '123@gmail.com', '+38095', 'kek')]

# with app.app_context():
    # db.create_all()
    # db.session.add(ModelPhoBook(
    #     name=list_PhoBook[0].name,
    #     surname=list_PhoBook[0].surname,
    #     mail = list_PhoBook[0].mail,
    #     phone = list_PhoBook[0].phone,
    #     note = list_PhoBook[0].note
    # ))
    # db.session.commit()


@app.route('/show')
def show():
    context = {
        'title': 'show',
        'menu': menu,
        'users': ModelPhoBook.query.all()
    }
    return render_template('show.html', context=context)


@app.route('/successful')
def successful():

    context = {
        'title': 'successful',
        'menu': menu,
        'add_user': db.session.execute(db.select(ModelPhoBook).order_by(ModelPhoBook.id)).scalars().first()
    }
    return render_template('successful.html', context=context)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = ModelPhoBook(
            name=request.form['name'],
            surname=request.form['surname'],
            mail=request.form['mail'],
            phone=request.form['phone'],
            note=request.form['note']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("successful"))
    context = {
        'title': 'Add user',
        'menu': menu
    }
    return render_template('main.html', context=context)


@app.route('/phone book')
def phone_phone():
    return redirect(url_for('index'))


@app.route('/edit/<int:user_id>')
def edit_element(user_id):
    p = ModelPhoBook.query.filter_by(id=user_id).first()
    data = {'name': p.name,
            'surname': p.surname,
            'mail': p.mail,
            'phone': p.phone,
            'note': p.note
            }
    response = make_response(jsonify(data))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.status_code = 200
    return response


@app.route('/delete/<int:user_id>')
def delete_element(user_id):
    p = ModelPhoBook.query.filter_by(id=user_id).first()
    db.session.delete(p)
    db.session.commit()
    data = {'answer': 'delete',
            }
    response = make_response(jsonify(data))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(debug=True)
