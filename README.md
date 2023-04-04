# Flask-SQLAlchemy-Project-Template
Ready to use template to understand Flask SQLAlchemy basic implementation, with examples. 
With Flask Blueprints and application factory. Avoids circular imports.

Minimalistic code and folder structure in the package.

## Introduction

Many tutorials on this topic are either old and non-working or complex.
SQLAlchemy is an Object Relational Mapper (ORM). You can work with Python class attributes
instead of raw SQL statements.

## Example
See the package in multi_server action as one of the [PyPi eisenmp_examples](https://pypi.org/project/eisenmp-examples/)

## How to create the SQLite Database?

Flask-SQLAlchemy can create the whole database file, tables and schema from your Python class definition.
The SQLALCHEMY_DATABASE_URI is used to create the database in the correct location with the given name.

models.py :

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String, unique=True, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False)
        profile = db.Column(db.String, unique=False, nullable=False)

__  init __.py  :

    this_dir = path.abspath(path.join(path.dirname("__file__")))
    db_path = path.join(this_dir, 'database.db')

    def create_app():
        ...
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
        db.init_app(app)  
        ...

    def setup_database(flask_app):
        with flask_app.app_context():
        # alchemy creates the db from SQLALCHEMY_DATABASE_URI and models.py classes
        db.create_all()

That's it!

Flask documentation says, that db.init_app(app) MUST be there, if application factory style is used.
## important Imports


 
database.py :

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

models.py :

    from .database import db



__  init __.py  :

    from .database import db

    def create_app():
        # flask initializes Alchemy with the application
        db.init_app(app)


/routes_users/routes_support.py :

	     from Flask_SQLAlchemy_Project_Template.database import db
         from Flask_SQLAlchemy_Project_Template.models import Users


## trip wires

Install flask-sqlalchemy and python interpreter into venv via pycharm file,settings,project,interpreter if 
it will not take place via the IDE window.

Circular import dilemma. Flask-SQLAlchemy is a candidate for hours of research and frustration.

## tips

Flask-sqlalchemy is dependent of the current context in the app. This will not show up in one file mini setups.
For bigger Flask apps, with multiple modules, it is obviously necessary to work with route(s) and blueprints.
This package also uses flask application factory. This is flask as a function ( def create_app(): ).


## run

    $ pip3 install Flask_SQLAlchemy_Project_Template
    $ python3 -m Flask_SQLAlchemy_Project_Template

## location

    $ pip3 show Flask_SQLAlchemy_Project_Template


## GitHub package
Just for the sake of my art. Not really useful, since you had to open the image to get the directory structure.

sudo docker run -v $(pwd):/alchemy -it --network host ghcr.io/44xtc44/flask_sqlalchemy_project_template:latest 

Connects your current dir with the docker image /alchemy dir. The app must write the database.

Cheers
