from flask import render_template

from app.birthday_calculator.forms import AnswerForm
from app.birthday_calculator import bp
from birthday_calculator import birthday_probability


@bp.route('/', methods=['GET', 'POST'])
def index():
    probability = None
    form = AnswerForm()
    if form.validate_on_submit():
        probability = birthday_probability(
            people=form.people.data,
            days_range=form.days_range.data,
            year_days=form.year_days.data
        )
    return render_template('index.html', title='Settings', form=form, probability=probability)
