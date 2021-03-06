import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from car_app.models import Event, Car, User
from flask_login import login_user, logout_user, login_required, current_user, UserMixin

from car_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # TODO: Make a query for all instances of 'User' and send to the template
    return render_template('home.html')
@main.route('/event_detail')
def event_detail():

    context = {
        'event': Event.query.filter_by(id=event_id).all()
    }
    return render_template('event_detail.html', ** context)

@main.route('/create_event')
@login_required
def create_event():
    form = EventForm()

    if form.validate_on_submit():

        new_event= Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(new_event)
        db.session.commit()

        flash('New Event was created!')
        return redirect(url_for('main.event_detail', event_id=new_event.id))
    return render_template('create_event.html', form=form)

@main.route('/create_car')
@login_required
def create_car():
    form = CarForm()

    if form.validate_on_submit():

        new_car= Car(
            make=form.make.data,
            model=form.model.data,
            year=form.year.data
        )
        db.session.add(new_event)
        db.session.commit()

        flash('New Car was added!')
        return redirect(url_for('main.event_detail', car_id=new_car.id))
    return render_template('create_car.html', form=form)
