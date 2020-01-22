from flask import Blueprint

bp = Blueprint('birthday_calculator', __name__)

from app.birthday_calculator import routes
