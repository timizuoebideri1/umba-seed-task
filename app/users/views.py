from decouple import config
from flask import Blueprint, request, render_template, url_for
from .models import Users

user_bp = Blueprint('users', __name__, template_folder='templates')


@user_bp.route('/')
def home():
    return render_template('users/index.html')
