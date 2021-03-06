from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from car_app.models import Event, Car, User




class EventForm(FlaskForm):
    """Form to create a Song."""
    title = StringField('Event Title', validators=[DataRequired(), Length(min=1, max=80)])
    date = DateField('Event Date')
    location = StringField('Event Location', validators=[DataRequired(), Length(min=1, max=80)])
    submit = SubmitField('Submit')


class CarForm(FlaskForm):
    """Form to create an Artist."""
    make = StringField('Car make', validators=[DataRequired(), Length(min=3, max=80)])
    model = TextAreaField('Car Model', validators=[DataRequired(), Length(min=3, max=80)])
    year = IntegerAreaField('Year Make', validators=[DataRequired(), max_length=200])
    submit = SubmitField('Submit')
