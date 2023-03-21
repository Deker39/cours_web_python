from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
import os
from main import main as main_blueprint

from models import Base, User
from urllib.parse import quote_plus
from sqlalchemy.engine import create_engine


#  driver: ///login:pass@host/db
engine = create_engine("mysql://root:26091998Asd@localhost/db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()


def start_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = os.urandom(12)
    app.config['SQLALCHEMY_DATABASE_URI'] = engine

    print(app.config)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    Base.metadata.create_all(engine)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main_blueprint)

    return app

# start_app()