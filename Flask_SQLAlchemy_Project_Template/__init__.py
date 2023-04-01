# install flask-sqlalchemy into venv via pycharm file,settings,project,interpreter (if problem)
from os import path
from flask import Flask
from .database import db

# import for creating test items, can be removed
from Flask_SQLAlchemy_Project_Template.models import Users, InternalUse

this_dir = path.abspath(path.join(path.dirname("__file__")))
db_path = path.join(this_dir, 'database.db')


def create_app(port=None):
    app = Flask(__name__)
    app.config['SERVER_PORT'] = port if port else None
    app.config['DEBUG'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"   # supress FSADeprecationWarning
    # flask initializes Alchemy with the application
    db. init_app(app)
    # Register Blueprints and routes, one route is also sufficient
    from Flask_SQLAlchemy_Project_Template.routes_internal import routes as internal_routes
    from Flask_SQLAlchemy_Project_Template.routes_user import routes as user_routes
    app.register_blueprint(internal_routes.internal_bp)
    app.register_blueprint(user_routes.user_bp)
    return app


def setup_database(flask_app):
    with flask_app.app_context():
        # alchemy creates the db from SQLALCHEMY_DATABASE_URI and models.py classes
        db.create_all()

        # only for test items, can be removed
        db.session.add(InternalUse(browser_open=1, statistics='98.6', commercials='sold'))
        db.session.add(InternalUse(browser_open=0, statistics=70.2, commercials='bid'))
        db.session.add(Users(username='pi', email='pi@pipapo.org', profile='ceo'))
        db.session.add(Users(username='pa', email='pa@pipapo.org', profile='chief'))
        db.session.add(Users(username='po', email='po@pipapo.org', profile='leader'))
        db.session.commit()
