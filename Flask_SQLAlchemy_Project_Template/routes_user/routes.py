import random

from flask import Blueprint, render_template, current_app, request
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
    """
    - Entry -

    Want an input mask with add and del user
    """
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    port = current_app.config['SERVER_PORT']
    print(f'server port {port}')
    return render_template('user_bp_index.html',
                           db_uri=db_uri,
                           port=port)


@user_bp.route('/user', methods=['GET'])
def user():
    """Show list of users
    dave is created once, then ignored by filter
    """
    user_dict = urs.list_users_db()
    html_user_list = []  # create an unordered list in html with jinja vars
    for dict_val in user_dict.values():
        html_user_list.append(dict_val)
    user_counter = urs.user_counter_db()
    return render_template('user_bp_content.html', table_dump=html_user_list, counter=user_counter)


@user_bp.route('/add_user_db', methods=['POST'])
def add_user_db():
    """Something add to delete later
    """
    pos = [
        'Web Developer', 'Desktop Support', 'Desktop Support', 'Software Engineer',
        'Data Entry', 'DevOps Engineer', 'Computer Programmer', 'Network Administrator',
        'Information Security Analyst', 'Artificial Intelligence Engineer', 'Cloud Architect',
        'IT Manager', 'Technical Specialist', 'Application Developer'
    ]
    request_dict = request.form.to_dict()

    user_name = request_dict['text_add_user_db_name']
    rv = urs.add_user_db(user_name, user_name + "@pipapo.org", random.choice(pos))
    msg = f'user {user_name} already exists' if not rv else f'{user_name} added, see server response.'
    urs.list_users_db()  # prints names in db
    return msg


@user_bp.route('/delete_user_db', methods=['POST'])
def delete_user_db():
    """Delete user by name"""
    request_dict = request.form.to_dict()

    user_name = request_dict['text_delete_user_db_name']
    rv = urs.del_user_db(user_name)
    msg = f'No user {user_name} in DB' if not rv else f'{user_name} deleted, see server response.'
    urs.list_users_db()  # prints names in db
    return msg
