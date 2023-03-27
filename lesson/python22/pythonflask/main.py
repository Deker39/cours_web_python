from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import  login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)

# app = Flask(__name__)

# TODO SQLAlchemy
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///f.db"
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     email = db.Column(db.String(120), unique=True, nullable=True)
#
#     def __repr__(self):  # __str__
#         return f"<User {self.name}>"
#
#
# with app.app_context():
#     db.create_all()
#
#     # user = User(name="Alex", email="mgrioegmr@gmail.com")
#     # db.session.add(user)
#     # db.session.commit()
#     users = User.query.all()
#     print(users)
#
#
# @app.route("/")
# def index():
#     return ""


# if __name__ == '__main__':
#     app.run(debug=True)
