import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from car_app.models import Event, Car, User

# Import app and db from events_app package so that we can run app
from car_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # TODO: Make a query for all instances of 'User' and send to the template
    return render_template('home.html')