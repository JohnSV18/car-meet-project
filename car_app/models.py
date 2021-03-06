from car_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin

class Car(db.Model):
    """Car Model"""
    id=db.Column(db.Integer, primary_key=True)
    brand_name=db.Column(db.String(100), nullable=False)
    model_name=db.Column(db.String(100), nullable=False)
    year_made=db.Column(db.Integer, primary_key=True)
    car_meets_attending = db.relationship('Event', secondary="car_event_table", back_populates='cars')
    

class Event(db.Model):
    """Event Model"""
    id= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    cars = db.relationship('Car', secondary='car_event_table', back_populates='car_meets_attending')

car_event_table = db.Table('car_event_table', 
    db.Column('car_id', db.Integer, db.ForeignKey('car.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    