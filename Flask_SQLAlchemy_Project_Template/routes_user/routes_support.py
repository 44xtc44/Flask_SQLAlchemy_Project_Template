
from sqlalchemy.exc import NoResultFound

from Flask_SQLAlchemy_Project_Template.database import db
from Flask_SQLAlchemy_Project_Template.models import Users


def add_user_db(user, email, profile):
    #  we have UNIQUE constraint for username and email in models.py
    success = True
    existing_user = Users.query.filter_by(username=user).first()
    existing_email = Users.query.filter_by(email=email).first()
    if not existing_user and not existing_email:
        db.session.add(Users(username=user, email=email, profile=profile))
        db.session.commit()
    else:
        success = False
    return success


def del_user_db(user):
    """Success
    We change the query.filter_by(...).one() here, not filter_by(...).first()
    only in case somebody wants to know that we have a unique constraint in DB
    if: more than one result, or no result returned - bam  interpreter exits

    We must use try now to calm interpreter.
    """
    existing_user = None
    success = True
    try:
        existing_user = Users.query.filter_by(username=user).one()
    except NoResultFound:
        success = False

    if existing_user:
        Users.query.filter(Users.username == user).delete()
        db.session.commit()
    else:
        success = False
    return success


def user_counter_db():
    return str(Users.query.count())


def list_users_db():
    users_table = Users.query.all()    # dump whole table users
    users_dict = {}
    for row in users_table:
        dict_val = 'name: ' + str(row.username) + ' ' + \
                   'email: ' + str(row.email) + ' ' + \
                   'profile: ' + str(row.profile)
        users_dict[row.id] = dict_val
        # print(row.id, row.username, row.profile)
        print(row.username)
    return users_dict
