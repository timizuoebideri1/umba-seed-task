from decouple import config
from flask import Blueprint, request, render_template, url_for
from .models import Users

user_bp = Blueprint('users', __name__, template_folder='templates')


@user_bp.route('/')
def home():
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('pagination', default=config("PAGE_SIZE", cast=int), type=int)
    users = Users.query.order_by(Users._id).paginate(page=page, per_page=page_size)

    return render_template('users/index.html', users=users, limit=page_size)
