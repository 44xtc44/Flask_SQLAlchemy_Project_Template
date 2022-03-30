from os import path
from flask import Blueprint, render_template, current_app
import Flask_SQLAlchemy_Project_Template.routes_user.routes_support as urs

# Blueprint Configuration
user_bp = Blueprint(
    'user_bp', __name__,
    template_folder='user_templates',
    static_folder='user_static',
    static_url_path='/user_static'
)


@user_bp.route('/', methods=['GET'])
def index():
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    return render_template('user_bp_index.html', db_uri=db_uri)


@user_bp.route('/user', methods=['GET'])
def user():
    urs.add_user_db("dave mops", "dave.mops@pipapo.org", "dev ops")

    user_dict = urs.list_users_db()
    html_user_list = []
    for dict_val in user_dict.values():
        html_user_list.append(dict_val)
    print(html_user_list)
    user_counter = urs.user_counter_db()
    return render_template('user_bp_content.html', table_dump=html_user_list, counter=user_counter)
