from flask_sqlalchemy import SQLAlchemy
# important! only partially initialized, no (app) and it is a 3rd party module
# initialized via db.init_app(app) in application factory (def create_app():)
db = SQLAlchemy()
