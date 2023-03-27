from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import User
from . import session

auth = Blueprint('auth', __name__)


@auth.route('/')
def signin():
    return render_template('login.html')


@auth.route('/signin', methods=['POST'])
def signin_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('please check you logi details and try again')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists')
        return redirect(url_for('auth.signup'))

    registered = User(username=username,
                      password=generate_password_hash(password, method='sha256'),
                      email=email)
    session.add(registered)
    session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    login_user()
    return redirect(url_for('main.index'))
