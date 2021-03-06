from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from car_app.models import Event, Car, User




class EventForm(FlaskForm):
    """Form to create a Song."""
    title = StringField('Song Title',
        validators=[DataRequired(), Length(min=1, max=80)])
    date = DateField('Date Released')
    location = QuerySelectField('Location',
        query_factory=lambda: Location.query, allow_blank=False)
    submit = SubmitField('Submit')


class CarForm(FlaskForm):
    """Form to create an Artist."""
    make = StringField('Artist Name',
        validators=[DataRequired(), Length(min=3, max=80)])
    model = TextAreaField('Information About Artist')
    year = IntegerAreaField
    submit = SubmitField('Submit')
