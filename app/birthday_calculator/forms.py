from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, validators


class AnswerForm(FlaskForm):
    people = IntegerField(
        'Number of people',
        [validators.NumberRange(min=0)],
        default=23,
    )
    days_range = IntegerField(
        'Number of days in a row',
        [validators.NumberRange(min=0)],
        default=0,
    )
    year_days = IntegerField(
        'Days a year',
        [validators.NumberRange(min=1)],
        default=365
    )
    submit = SubmitField('Calculate')
