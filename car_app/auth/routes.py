from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from car_app.models import Event, Car, User
from car_app.auth.forms import SignUpForm, LoginForm
from car_app import bcrypt

# Import app and db from events_app package so that we can run app
from car_app import app, db

auth = Blueprint("auth", __name__)

##########################################
#           Routes                       #
##########################################

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Signup Route'''
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        flash('Account Created.')
        return redirect(url_for('auth.login'))
    print(form.errors)
    return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Login Route'''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        next_page = request.args.get('next')
        return redirect(next_page if next_page else url_for('main.home'))
    print(form.errors)
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    '''Logout Route'''
    logout_user()
    return redirect(url_for('main.home'))
